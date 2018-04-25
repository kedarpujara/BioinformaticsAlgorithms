   public static String findLCS_String(String x, String y)
   {
      int mid, i, j;
      int m, n;
      String C = "";

      m = x.length();           // m = length of x
      n = y.length();           // n = length of y


      /* =====================================================
         Base case 1: ""
         ===================================================== */
      if ( m == 0 )
      {
         return "";             // LCS = ""
      }

      /* =====================================================
         Base case 2: x = "?"
         ===================================================== */
      if ( m == 1 )
      {
         /* =====================================
            The input x consists of 1 character
            Find the single common character in y
            ===================================== */
         for ( i = 0; i < n; i++ )
            if ( y.charAt(i) == x.charAt(0) )
               return( x );                   // Found: LCS = x

         return "";                           // Not found: LCS = ""
      }

      /* =====================================================
         General case:  x has 2 or more characters
         ===================================================== */

      String x1="", x2="";          // x1 = first half of x, x2 = second half
      int    c1=0,  c2=0;           // c1 = length of first LCS, c2 = second

      int c = solveLCS( x, y ) ;    // This is the sum of the correct split

      x1 = x.substring( 0, m/2 );   // First half of x
      x2 = x.substring( m/2, m );   // Second half of x

      /* --------------------------------------------------
         Find a correct split of y
         -------------------------------------------------- */
      for ( k = 0; k < n; k++ )
      {
          c1 = solveLCS( x1, y.substring(0, k) ) ; // LCS of first half
          c2 = solveLCS( x2, y.substring(k, n) ) ; // LCS of second half

          if ( c1 + c2 == c )
             break;             // Found a correct split of y !!!
      }

      /* --------------------------------------------------
         Here: k = a correct split location of y ....

         Solve smaller problems
         -------------------------------------------------- */

      String y1 = y.substring( 0, k );
      String y2 = y.substring( k, n );

      String sol1 = findLCS_String( x1, y1 );
      String sol2 = findLCS_String( x2, y2 );

      /* ------------------------------------------------------------
         Use solution of smaller problems to solve original problem
         ------------------------------------------------------------ */
      return ( sol1 + sol2 );
   }

public static void main(String[] args) {

   String string1 = "AACCTTGG";
   String string2 = "ACACTGTGA";
   String stringRet = new findLCS_String(string1,string2);
   System.out.println(stringRet);
}