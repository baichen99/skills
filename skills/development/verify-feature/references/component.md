# Component and composition checks

Run the target project's real components. The scope may be a single field,
a form with validation, or a connected list/dialog/drawer composition.

1. Inspect source, framework version, existing tests/stories, styles, and build configuration.
2. Reuse the established renderer or harness and its normal lifecycle cleanup.
3. Supply required props, providers, stores, routing, plugins, and configuration.
4. Keep the behavior under test real: handlers, state updates, validation,
   request clients, and participating child components.
5. Mock peripheral dependencies at the boundary and state exactly what was substituted.
6. Test visible behavior. Use a real browser for layout, focus, CSS, and screenshots.

| Stack | Typical existing entry point | Environment to preserve |
| --- | --- | --- |
| React / Next.js | Testing Library, Storybook, component runner, app route | Providers, router, server/client boundary, styles |
| Vue / Nuxt | Vue Test Utils, Testing Library, Storybook, app route | Plugins, store, router, styles |
| Svelte / SvelteKit | Testing Library, Storybook, app route | Context, stores, client/server loading, styles |
| Angular | TestBed, existing browser tests, app route | Injection, router, forms, styles |
| Web Components / vanilla | Real DOM mount or existing page/runner | Custom-element registration, shadow DOM, events, styles |

These are discovery hints, not instructions to install another framework or
runner. Follow the target framework's installed version and project conventions.
Use an actual app route when isolation would replace the behavior being checked,
such as server rendering, middleware, hydration, or host-provided data.

Prefer network-boundary mocks when requests are part of the feature. Preserve
URL/method matching and raw field types. Model loading, failure, empty data,
delayed responses, and reset behavior only as needed for the requested cases.

Report the mounted components, injected environment, mocked boundaries, and style
coverage. Injected route data does not verify host routing. A DOM-only renderer
does not verify layout. A passing component composition does not verify the real
backend or the entire application.
