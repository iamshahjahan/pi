Working on different projects.

1. Coupons


   ![Coupon diagram](./src/coupon/coupan.png?raw=true "Title")

2. Email using Celery
   
3. LRU Cache

4. In memory Search Engine for Book Shop using Typeahead
   ![Coupon diagram](./src/booksearch/booksearch.png?raw=true "Title")
    i.  User should be able to search by 
        a. author
        b. title
        c. publisher
    

    Book
        -- book id
        -- title
        -- publisher

    BookItem
        -- book item id
        -- Book
        -- ISBN code

    Author
        -- author name
        -- author id

    Inventory
        -- BookItem
    
    Search
        -- books by title
        -- books by publisher
        -- books by author
        
        -- search_by_title
        -- search_by_publisher
        -- search_by_author

    title_dict = {
        title: [book_id],
    }
    
    abcd --> bc --> True
        --> bd --> False
    
    chetan
    he --> 

    %query%
            --> contains max(o(n1) + O(n2) + O(n3))*max(len(title),len(publisher),len())
    %bha% --> chetan
          --> bhartiya publication
    author_dict = {
        author: [book_ids],
    }

    publisher_dict = {
            publisher: [book_ids],
        }

    