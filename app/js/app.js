$(document).ready(function() {
    $('#content').load('components/content.html', function() {
      $('#myButton').click(function() {
        const card = `
          <div class="card col-md-4">
            <div class="card-body">
              <h5 class="card-title">Card Title</h5>
              <p class="card-text">This is a card.</p>
              <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
          </div>
        `;
        $('#cardContainer').append(card);
      });
    });
  });
  