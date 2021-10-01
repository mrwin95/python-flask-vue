<template>
   <div class="container">
       <div class="row">
           <div class="col-sm-10">
               <h1>Book List</h1>
               <hr> <br>

               <table class="table table-hover">
                   <thead>
                       <tr>
                           <th>Title</th>
                           <th>Author</th>
                           <th>Read?</th>
                           <th>Price</th>
                           <th></th>
                       </tr>
                   </thead>
                   <tbody>
                       <tr v-for="(book, index) in books" :key="index">
                           <td>{{book.title}}</td>
                           <td>{{book.author}}</td>
                           <td>{{book.read}}</td>
                           <td>{{book.price}}</td>
                           <td>
                               <button type="button" class="btn btn-warning">Update</button>                               
                               <button type="button" class="btn btn-danger">Delete</button>
                           </td>
                       </tr>
                   </tbody>
               </table>
           </div>
       </div>
    </div> 
</template>

<script>
import axios from 'axios';
export default {
    name: 'BookList',
    data() {
        return {
            books: []
        }
    },

    methods: {        
        all_books(){
            const path = 'http://localhost:5000/books';
            axios.get(path).then((res) => {
                this.books = res.data.books;
            }).catch((err) => {
                console.log(err)
            })
        }
    },

    created() {
        this.all_books()
    }
}
</script>