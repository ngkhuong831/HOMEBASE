CREATE PROCEDURE ManagePosts
(
    @PostID INT = NULL,
    @Title VARCHAR(255) = NULL,
    @Content TEXT = NULL,
    @Author VARCHAR(100) = NULL,
    @Action VARCHAR(10),
    @CommentID INT = NULL,
    @CommentContent VARCHAR(255) = NULL,
    @UserID INT = NULL,
    @FetchRelatedData BIT = 0
)
AS
BEGIN
CASE
    WHEN @Action = 'AddPost' THEN 
    BEGIN
        INSERT INTO Posts (Title, Content, Author)
        VALUES (@Title, @Content, @Author);
    END
    
    WHEN @Action = 'GetDetails' THEN 
    BEGIN
        SELECT PostID, Title, Content, Author
        FROM Posts
        WHERE PostID = @PostID;
    END
    
    WHEN @Action = 'UpdatePost' THEN 
    BEGIN
        UPDATE Posts
        SET Title = @Title,
            Content = @Content,
            Author = @Author
        WHERE PostID = @PostID;
    END
    
    WHEN @Action = 'DeletePost' THEN 
    BEGIN
        DELETE FROM Posts
        WHERE PostID = @PostID;
    END
    IF @Action = 'AddComment'
    BEGIN
        INSERT INTO Comments (PostID, Content, UserID)
        VALUES (@PostID, @CommentContent, @UserID);
    END
    
    WHEN @Action = 'DeleteComment' THEN 
    BEGIN
        DELETE FROM Comments
        WHERE CommentID = @CommentID;
    END
    
    WHEN @Action = 'FetchData' THEN 
    BEGIN
        IF @FetchRelatedData = 1
        BEGIN
            SELECT c.CommentID, c.Content, u.Username
            FROM Comments AS c
            INNER JOIN Users AS u ON c.UserID = u.UserID
            WHERE c.PostID = @PostID;
        END
    END
END