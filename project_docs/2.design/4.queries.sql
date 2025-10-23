select * from posts
select * from users
select * from votes

delete from users where id=1

SELECT title, content, email 
FROM posts p 
LEFT JOIN users u ON p.owner_id = u.id;

SELECT u.id, u.email, COUNT(p.id) as user_post_count 
FROM posts p RIGHT JOIN users u ON p.owner_id = u.id 
GROUP BY u.id;

SELECT * FROM posts 
LEFT JOIN votes ON posts.id = votes.post_id

SELECT posts.id, COUNT(votes.post_id)
FROM posts 
LEFT JOIN votes ON posts.id = votes.post_id
-- WHERE votes.post_id = 6
GROUP BY posts.id


SELECT posts.id AS posts_id, posts.title AS posts_title, posts.content AS posts_content, posts.published AS posts_published, posts.created_at AS posts_created_at, posts.owner_id AS posts_owner_id, count(votes.post_id) AS votes 
FROM posts
LEFT OUTER JOIN votes ON votes.post_id = posts.id
WHERE posts.published = true
GROUP BY posts.id


