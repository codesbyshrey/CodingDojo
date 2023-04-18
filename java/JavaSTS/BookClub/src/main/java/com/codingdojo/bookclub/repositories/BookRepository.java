package com.codingdojo.bookclub.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.codingdojo.bookclub.models.Book;

@Repository //
public interface BookRepository extends CrudRepository<Book, Long> {
	List<Book> findAll();
	// Find all books JPA
}
