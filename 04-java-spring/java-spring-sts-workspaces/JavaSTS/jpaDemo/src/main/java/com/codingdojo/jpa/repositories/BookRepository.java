package com.codingdojo.jpa.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.codingdojo.jpa.models.Book;

//...
@Repository
public interface BookRepository extends CrudRepository<Book, Long>{
 // this method retrieves all the books from the database
 List<Book> findAll();
 
 // this method finds books with descriptions containing the search string
 List<Book> findByDescriptionContaining(String search);
 
 List<Book> findByTitleIs(String title); //implements the query and search all at once
 // will find by a direct title name from documentation
 
 // this method counts how many titles contain a certain string
 Long countByTitleContaining(String search);
 
 // this method deletes a book that starts with a specific title
 Long deleteByTitleStartingWith(String search);
}

