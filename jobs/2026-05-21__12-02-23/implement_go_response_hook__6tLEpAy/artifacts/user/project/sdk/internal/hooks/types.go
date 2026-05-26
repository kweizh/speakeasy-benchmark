package hooks

import (
	"net/http"
)

type AfterSuccessContext struct {
	HookContext
}

type AfterSuccessHook interface {
	AfterSuccess(ctx AfterSuccessContext, res *http.Response) (*http.Response, error)
}

type BeforeRequestContext struct {
	HookContext
}

type BeforeRequestHook interface {
	BeforeRequest(ctx BeforeRequestContext, req *http.Request) (*http.Request, error)
}

type AfterErrorContext struct {
	HookContext
}

type AfterErrorHook interface {
	AfterError(ctx AfterErrorContext, res *http.Response, err error) (*http.Response, error)
}

type HookContext struct {
	OperationID string
}

type Hooks struct {
	beforeRequestHooks []BeforeRequestHook
	afterSuccessHooks  []AfterSuccessHook
	afterErrorHooks    []AfterErrorHook
}

func (h *Hooks) RegisterBeforeRequestHook(hook BeforeRequestHook) {
	h.beforeRequestHooks = append(h.beforeRequestHooks, hook)
}

func (h *Hooks) RegisterAfterSuccessHook(hook AfterSuccessHook) {
	h.afterSuccessHooks = append(h.afterSuccessHooks, hook)
}

func (h *Hooks) RegisterAfterErrorHook(hook AfterErrorHook) {
	h.afterErrorHooks = append(h.afterErrorHooks, hook)
}

func NewHooks() *Hooks {
	return &Hooks{
		beforeRequestHooks: []BeforeRequestHook{},
		afterSuccessHooks:  []AfterSuccessHook{},
		afterErrorHooks:    []AfterErrorHook{},
	}
}
