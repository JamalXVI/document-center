<!-- Svelte-based Navbar Component -->
<script>
    import { isLoggedIn } from '../stores';
  </script>
  
  <style>
    @import 'bulma/css/bulma.css';
  </style>
  
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="#">
        Academic Documentation Center
      </a>
    </div>
  
    <div id="navbarBasicExample" class="navbar-menu">
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            {#if !$isLoggedIn}
              <a class="button is-primary" href="/login">
                <strong>Login</strong>
              </a>
            {/if}
          </div>
        </div>
      </div>
    </div>
  </nav>