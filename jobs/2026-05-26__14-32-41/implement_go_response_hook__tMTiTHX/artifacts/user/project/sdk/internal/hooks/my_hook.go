package hooks

import (
	"net/http"
)

type MyResponseHook struct{}

func (h *MyResponseHook) AfterSuccess(hookCtx AfterSuccessContext, res *http.Response) (*http.Response, error) {
	if res.Header == nil {
		res.Header = make(http.Header)
	}
	res.Header.Set("X-Hook-Injected", "true")
	return res, nil
}
