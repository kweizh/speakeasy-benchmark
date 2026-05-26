package hooks

import "net/http"

// InjectHeaderHook implements AfterSuccessHook and injects the
// X-Hook-Injected: true header into every successful HTTP response.
type InjectHeaderHook struct{}

// AfterSuccess is called after every successful HTTP response. It ensures the
// response header map is initialised and sets X-Hook-Injected to "true".
func (h *InjectHeaderHook) AfterSuccess(_ HookContext, res *http.Response) (*http.Response, error) {
	if res.Header == nil {
		res.Header = make(http.Header)
	}
	res.Header.Set("X-Hook-Injected", "true")
	return res, nil
}
