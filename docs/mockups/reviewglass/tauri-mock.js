// A stand-in for the Tauri core, so ReviewGlass's own pages render in a browser.
// Every answer is staged: window.__RG_MOCK__ (set by the capture script before this runs)
// carries the window's label, its size, the glass state and the source picture's URL.
(() => {
  const M = window.__RG_MOCK__ || {};
  const callbacks = new Map();
  let nextId = 1;
  const listeners = [];

  let source = null; // { w, h, data } RGBA of the staged screen
  let seq = 1;
  if (M.sourceUrl) {
    const img = new Image();
    img.crossOrigin = "anonymous";
    img.onload = () => {
      const c = document.createElement("canvas");
      c.width = img.naturalWidth;
      c.height = img.naturalHeight;
      const x = c.getContext("2d");
      x.drawImage(img, 0, 0);
      source = { w: c.width, h: c.height, data: x.getImageData(0, 0, c.width, c.height).data };
      seq++;
    };
    img.src = M.sourceUrl;
  }

  let view = { w: 0, h: 0 };
  function frame(since) {
    if (!source || view.w < 2 || since >= seq) return new ArrayBuffer(0);
    const zoom = M.state.zoom;
    // The core hands over the source at 1:1: the picture's size divided by the zoom,
    // read around the staged cursor.
    const sw = Math.max(1, Math.round(view.w / zoom));
    const sh = Math.max(1, Math.round(view.h / zoom));
    const ox = Math.max(0, Math.min(source.w - sw, Math.round(M.cursor.x - sw / 2)));
    const oy = Math.max(0, Math.min(source.h - sh, Math.round(M.cursor.y - sh / 2)));
    const buf = new ArrayBuffer(16 + sw * sh * 4);
    const dv = new DataView(buf);
    dv.setBigUint64(0, BigInt(seq), true);
    dv.setUint32(8, sw, true);
    dv.setUint32(12, sh, true);
    const out = new Uint8ClampedArray(buf, 16);
    for (let y = 0; y < sh; y++) {
      const from = ((oy + y) * source.w + ox) * 4;
      out.set(source.data.subarray(from, from + sw * 4), y * sw * 4);
    }
    return buf;
  }

  const answers = {
    glass_state: () => M.state,
    glass_set_view: (a) => {
      view = { w: a.widthPx, h: a.heightPx };
      seq++;
      return a.zoom;
    },
    glass_frame: (a) => frame(a.since),
    frame_state: () => M.frame,
    diffwin_is_open: () => !!M.diffOpen,
    "plugin:window|outer_position": () => ({ x: 0, y: 0 }),
    "plugin:window|inner_position": () => ({ x: 0, y: 0 }),
    "plugin:window|inner_size": () => ({ width: innerWidth, height: innerHeight }),
    "plugin:window|outer_size": () => ({ width: innerWidth, height: innerHeight }),
    "plugin:window|scale_factor": () => devicePixelRatio,
    "plugin:event|listen": (a) => {
      listeners.push(a);
      return nextId++;
    },
    "plugin:event|unlisten": () => null,
  };
  Object.assign(answers, M.answers || {});

  window.__RG_EMIT__ = (event, payload) => {
    for (const l of listeners) {
      if (l.event !== event) continue;
      const cb = callbacks.get(l.handler);
      if (cb) cb({ event, id: 0, payload });
    }
  };
  window.__RG_CALLS__ = [];

  window.__TAURI_INTERNALS__ = {
    metadata: {
      currentWindow: { label: M.label || "glass" },
      currentWebview: { windowLabel: M.label || "glass", label: M.label || "glass" },
    },
    transformCallback(cb, once) {
      const id = nextId++;
      callbacks.set(id, cb);
      return id;
    },
    unregisterCallback(id) {
      callbacks.delete(id);
    },
    convertFileSrc: (p) => p,
    async invoke(cmd, args) {
      window.__RG_CALLS__.push(cmd);
      const f = answers[cmd];
      if (typeof f === "function") return f(args || {});
      if (f !== undefined) return f;
      return null;
    },
  };
  window.__TAURI_EVENT_PLUGIN_INTERNALS__ = { unregisterListener() {} };
})();
