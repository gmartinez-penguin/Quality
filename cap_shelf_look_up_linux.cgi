#!/opt/ActivePerl-5.24/bin/perl5

use CGI qw(:standard);
use DBI;

print header,
start_html(-title=>'Capacitor Shelf Form',
            -BGCOLOR=>'skyblue'),

h2("Welcome to the Penguin Capacitor Shelf Database Look up Program...");

if (param){
   &do_work();
}
else {
   &print_form();
}


#print end_html;

sub print_form{
   print start_form(-name=>"form1", -id=>"form1");

   $dbh = DBI->connect('DBI:mysql:production:127.0.0.1','') or print "\n Can not connect to Database, please contact Gary to resolve.  " , DBI->errstr;

    my $sth=$dbh->prepare("select * from cap_shelf");
    $sth->execute();

   print "<div align='center'>";

   while (my @val = $sth->fetchrow_array()) {
          $timer->{$val[2]}->{$val[0]}=$val[3];
   }

   print h2("The following Capacitor Shelves are in the MySQL Database:");

   print qq/<table border="1" cellpadding="10" bgcolor="lightyellow">/;

   print <<TH1;
         <tr>
              <th>Order_ID</th>
              <th>Date_Time</th>
              <th>Serial_Number</th>
       </tr>
TH1


foreach $dates (reverse sort keys %{$timer}){
   while (( $ids,$sns)=each(%{$timer->{$dates}})){
             print <<EOF1;
                   <tr align="center">
                        <td><a href="cap_shelf_look_up.cgi?id=$ids&sn=$sns&date_time=$dates"> $ids </a></td>
                        <td nowrap>$dates</td>
                        <td nowrap>$sns</td>
                   </tr>
EOF1

                                                                                      }
}

     print "</table>";
     print "<BR>";
     print "<BR>";

                                                                                #print end_html();

   $sth->finish();
   $dbh->disconnect();


}


sub do_work {

   print "<BR>";

   my $dbh = DBI->connect('DBI:mysql:production:127.0.0.1','') or print "\n Can not connect to Database, please contact Gary to resolve.  " , DBI->errstr;

   $id = param('id');
   $sn = param('sn');
   $datetimes = param('date_time');

   my $sth=$dbh->prepare("select * from cap_shelf
                              where Order_Id = ? and Date_Time = ? and Serial_Number = ?");

   print h2("You selected the following: Order_ID=$id, Date_Time=$datetimes, Serial_Number=$sn");

   $sth->execute($id,$datetimes,$sn);

   print "<div align='center'>";
   print qq/<table border="1" cellpadding="10" bgcolor="lightyellow">/;

   print <<TH;
        <tr>
            <th>Order_ID</th>
            <th>Tester</th>
            <th>Date_Time</th>
            <th>Serial_Number</th>
            <th>Assembly_Steps</th>
            <th>Assembly_Performed</th>
            <th>Test_Sequences</th>
            <th>Cap1</th>
            <th>Cap2</th>
            <th>Cap3</th>
            <th>Cap4</th>
            <th>Cap5</th>
            <th>Cap6</th>
            <th>Cap1_mvdc</th>
            <th>CB1_Resets</th>
            <th>Cap2_mvdc</th>
            <th>CB2_Resets</th>
            <th>Cap3_mvdc</th>
            <th>CB3_Resets</th>
            <th>Cap4_mvdc</th>
            <th>CB4_Resets</th>
            <th>Cap5_mvdc</th>
            <th>CB5_Resets</th>
            <th>Cap6_mvdc</th>
            <th>CB6_Resets</th>
            <th>TestResult</th>
       </tr>
TH


   while (my @val = $sth->fetchrow_array()) {
       print <<EOF;
           <tr align="center">
                <td>$val[0]</td>
                <td nowrap>$val[1]</td>
                <td nowrap>$val[2]</td>
                <td nowrap>$val[3]</td>
                <td nowrap>$val[4]</td>
                <td>$val[5]</td>
                <td nowrap>$val[6]</td>
                <td>$val[7]</td>
                <td>$val[8]</td>
                <td>$val[9]</td>
                <td>$val[10]</td>
                <td>$val[11]</td>
                <td>$val[12]</td>
                <td>$val[13]</td>
                <td>$val[14]</td>
                <td>$val[15]</td>
                <td>$val[16]</td>
                <td>$val[17]</td>
                <td>$val[18]</td>
                <td>$val[19]</td>
                <td>$val[20]</td>
                <td>$val[21]</td>
                <td>$val[22]</td>
                <td>$val[23]</td>
                <td>$val[24]</td>
                <td>$val[25]</td>


           </tr>

EOF


    }

    print "</table>";
    print "<BR>";
    print "<BR>";



    $sth->finish();
    $dbh->disconnect();


}




  
