<!-- Svelte-based Home Page -->
<script>
    import { onMount } from 'svelte';
    import Navbar from '../components/Navbar.svelte';
    import { documents, fetchDocuments } from '../utils/fetchDocuments';
  
    // Fetch documents when the page loads
    onMount(() => {
      fetchDocuments();
    });
  </script>
  
  <style>
    @import 'bulma/css/bulma.css';
  </style>
  
  <Navbar />
  
  <section class="section">
    <div class="container">
      <h1 class="title">Documents</h1>
      <table class="table is-striped is-fullwidth">
        <thead>
          <tr>
            <th>Title</th>
            <th>Description</th>
            <th>Author</th>
            <th>Department</th>
            <th>Publication Date</th>
          </tr>
        </thead>
        <tbody>
          {#each $documents as doc}
            <tr>
              <td>{doc.title}</td>
              <td>{doc.description || ''}</td>
              <td>{doc.author || ''}</td>
              <td>{doc.department || ''}</td>
              <td>{doc.publication_date || ''}</td>
            </tr>
          {/each}
        </tbody>
      </table>
    </div>
  </section>