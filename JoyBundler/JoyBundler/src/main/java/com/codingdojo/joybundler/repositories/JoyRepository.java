package com.codingdojo.joybundler.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.codingdojo.joybundler.models.Joy;

@Repository
public interface JoyRepository extends CrudRepository<Joy, Long>{
	
	List<Joy> findAll();
	
	// using specific terminology will let you access specific queries
	// SQL specific language / model specific language
}
