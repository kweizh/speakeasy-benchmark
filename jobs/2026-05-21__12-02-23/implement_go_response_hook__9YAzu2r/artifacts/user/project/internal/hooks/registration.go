package hooks

func initHooks(h *Hooks) {
	h.RegisterAfterSuccessHook(&ResponseHook{})
}
