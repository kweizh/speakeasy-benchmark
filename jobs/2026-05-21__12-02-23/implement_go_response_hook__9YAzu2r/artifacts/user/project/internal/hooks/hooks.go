package hooks

import (
	"net/http"
)

type ResponseHook struct{}

func (h *ResponseHook) AfterSuccess(hookContext AfterSuccessContext, res *http.Response) (*http.Response, error) {
	res.Header.Add("X-Hook-Injected", "true")
	return res, nil
}
