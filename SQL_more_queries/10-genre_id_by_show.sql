-- Task 10
-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM shows
JOIN tv_shows ON tv_show_genres.genre_id = title.id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC
