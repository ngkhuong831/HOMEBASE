# ManagePosts Stored Procedure
## Parameters

- `@PostID INT`
- `@Title VARCHAR(255)`
- `@Content TEXT` Using TEXT for the contents of post may get very lengthy
- `@Author VARCHAR(100)`
- `@Action VARCHAR(10)` Use to specify action to be conducted
- `@CommentID INT`
- `@CommentContent VARCHAR(255)`
- `@UserID INT`
- `@FetchRelatedData BIT` Flag to know whether or not to fetch related data

## Actions

- `AddPost`
- `GetDetails`
- `UpdatePost`
- `DeletePost`
- `AddComment`
- `DeleteComment`
- `FetchData`

