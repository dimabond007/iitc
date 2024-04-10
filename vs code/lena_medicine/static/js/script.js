var splide = new Splide( '.splide' , {
    type   : 'loop',
    autoplay:true,
  } );
splide.on( 'autoplay:playing', function ( rate ) {
  console.log( rate ); // 0-1
} );

splide.mount();