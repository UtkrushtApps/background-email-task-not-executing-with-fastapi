### Task Overview

A SaaS startup’s onboarding flow requires that a welcome email be sent automatically and asynchronously to all new users upon successful registration. However, the current FastAPI implementation is not sending emails as a background process, so no emails are received after registration, impacting the onboarding experience and user satisfaction.

### Guidance

- All user registration logic should remain responsive by not blocking during email operations
- The background email dispatch should trigger seamlessly after a new user is created
- Use the appropriate FastAPI techniques for background tasks, avoiding any synchronous email-sending that might block event handling
- Pay attention to async/await patterns for proper concurrency handling
- Code organization and modularity are expected for maintainability
- Handle any exceptions in background tasks to prevent silent failures

### Objectives

- Implement a FastAPI registration endpoint that correctly triggers a background job for email sending
- Ensure successful responses even if the email task is still in progress
- Use dependency injection and FastAPI’s background task system properly
- Validate that asynchronous patterns are respected and the main request/response cycle is not blocked

### How to Verify

- Register a new user and confirm that the API response returns immediately, not after any simulated email delay
- Inspect logs/output to ensure the background email-sending function is executed shortly after registration
- Confirm that users can continue to register even if many email tasks are being processed in the background
- Check that exceptions in the email task do not crash or affect the main API workflow
