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

5. Parking lot design
   
    -- a vehicle enters from one of the entry gates
   
    -- parking attendant generates a ticket for the vehicle
   
    -- vehicle gets parked at a location
   
    -- vehicle comes to one of the exit gate.
   
    -- payment happens and parking spot gets vacated.
   
    ![Parking diagram](./src/parkinglot/parkinglot.png?raw=true "Title")
   
6. docker images:

    login to mysql:
   
        mysql -h localhost -P 3308 --protocol=tcp -u user -ppassword

        Remove a file from git: git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch  src/docker_mysql_mongod_sqs_s3/docker/provision/mysql/init/01-databases.sql'  --prune-empty --tag-name-filter cat -- --all

7. Design splitwise:
    Expense management system.
       
    Requirements:
   
    1. user can create a group.
    2. user can add bill:
        i. split strategy:
            a. equal
            b. percentage
            c. exact
        ii. paid
        iii. total amount
       
    
    -------
    1. User level Expense
    2. Group level Expense
        i. five people are there and paid by you: equally divide.
        ii. five people are there and paid by two, should be divided equally.
        iii. Five people are there and paid by two, one person has higher percentage.
    
    3. History of bills generated.

    Actors:
        1. User
        2. Application
    
    Actions:
        1. User can add a bill
        
            Bill:
                i.   users involved.
                ii.  total amount.
                iii. expense: 
                        users
                        strategy
                            i. equal
                            ii. percentage
                                <user, percentage>        
                iv. payment:
                        <user, amount>
        
        2. User can do the settlement
            
            Can happen at user level.
            Can happen at group level.