#!/usr/bin/node

const request = require('request')
const movieId = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

if (!movieId) {
	console.error('Usage: ./0-starwars_characters.js <Movie ID>');
	process.exit(1);
}

request(`${API_URL}${movieId}/`, (err, response, body) => {
	if (err) {
		console.error(err);
		return;
	}
	const charactersURL = JSON.parse(body).characters;
	const charactersName = charactersURL.map(
		url => new Promise((resolve, reject) => {
			request(url, (promiseErr, _, charactersReqBody) => {
				if (promiseErr) {
					reject(promiseErr);
				}
				resolve(JSON.parse(charactersReqBody).name);
			});
		})
	);

	Promise.all(charactersName)
	.then(names => console.log(names.join('\n')))
	.catch(allErr => console.error(allErr));
});
