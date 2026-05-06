Service
	public Genre createOrRetrieve(String genreName) {
		Optional<Genre> mightExist = genreRepo.findGenreByName(genreName);
		if (mightExist.isPresent()) {
			return mightExist.get();
		} else {
			return genreRepo.save(new Genre(genreName));
		}
	}

	public Game createGameWithGenres(Game newGamePlus) {
		List<Genre> genres = new ArrayList<Genre>();
		for (String genreName : newGamePlus.getGenresInput().split(",")) {
			genres.add(createOrRetrieve(genreName));
		}
		newGamePlus.setGenres(genres);
		return gameRepo.save(newGamePlus);
	}