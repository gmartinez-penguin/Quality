#!/opt/ActivePerl-5.24/bin/perl5

use CGI qw(:standard);

=pod
print '<html>';
print '<head>';
print '<title>Simple html</title>';
print '</head>';
print '<body>';
print '<h1>Sample</h1>';
print '</body>';
print '</html>';

use CGI qw(:standard);
=cut


use DBI;

$TEST = 9;

print header,
start_html(-title=>'Capacitor Shelf Form',
           -BGCOLOR=>'skyblue' ),

h2("Welcome to the Penguin Capacitor Shelf Test... ");

&print_form();
&do_work() if(param);
print end_html;


sub print_form{

   print start_form(-name=>"form1", -id=>"form1");

   print h2("Check Capacitor Shelf Assembly according to the Build Instructions:");
   print "<table align='center' cellpadding='10' border='2' bgcolor='lightyellow'>";

   print "<tr>";
   print "<td>Front Panel Centered and Properly Oriented?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'front_panel_center',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     

   print "</td>";

   print "<td>Front Panel Handles Screwed down tight?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'handles',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";
   print "</tr>";

   print "<tr>";
   print "<td>LED's Seated Properly onto Holder & Ring?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'led_seat',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   
   print "<td>LED's Oriented Correctly- Top to Bottom(Green/Yellow/Red)?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'led_orient',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     

   print "</td>";
   print "</tr>";

   print "<tr>";
   print "<td>BNC Cable Properly Installed and Screws Tightened?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'bnc_cable',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>Discharge Flush Switch Installed?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'discharge_flush',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";
   print "</tr>";


   print "<tr>";
   print "<td>Discharge in Correct Orientation and Cables Installed?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'discharge_orient',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     

   print "</td>";

   print "<td>M3 Screws on Circuit Breakers Tightened? (PN:10025017)";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'cb_screws',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";
   print "</tr>";

   print "<tr>";
   print "<td>M3 Screws on BusBar Clips Tightened? (PN:10025017)";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'busbar',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";
   

   
   print "<td>12V Cable (RED) Installed onto Breaker with Split Washer locked?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'cb_red',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     

   print "</td>";
   print "</tr>";

   print "<tr>";
   print "<td>12V Cable (RED) Below Surface Wiring?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'surface',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>12V Cable (RED) Installed onto Correct Circuit Breaker (1 For 1)?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'cb_cables',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";
   print "</tr>";

   print "<tr>";
   print "<td>6 Gauge Cable From Breaker to Capacitor * Nut Tightened * ?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'gauge6',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>Positive Cable (RED) on Capacitor using M6 Screw + Split/Flat Torque 50 Inch lb?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'red50',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";
   print "</tr>";

   print "<tr>";
   print "<td>Negative Cable (BLACK) on Capacitor using M6 Screw + Split/Flat Torque 50 Inch lb?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'black50',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>Current Sense Ring Cable placed onto Negative (Black) cable connected to Capacitor?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'sense',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";
   print "</tr>";

   print "<tr>";
   print "<td>Current Sense Ring Cable (Green Dot facing away from Capacitor)?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'green_dot',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>Negative Discharge Cable (Black) Installed in All Capacitors?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'neg_discharge',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";
   print "</tr>";


   print "<tr>";
   print "<td>PCA Board * Correct Cable Placed Onto Correct Channel * ?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'pca',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>12V Fan Cable on PCA Board No. 3 & 4?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'fan',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";
   print "</tr>";

   print "<tr>";
   print "<td>Cables Properly Grouped and Tie Wrapped * away from risk of damage *?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'grouped',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>";
   print "</td>";
   print "<td>";
#   print radio_group(-name=>'color3',
#                     -values=>['Yes', 'No'],
#                     -default=>'No',
#                     -linebreak=>'1',
#                   );     
   print "</td>";
   print "</tr>";




   print "</table>";


   print h2("Check Capacitor Shelf LED Operation:");
   print "<table align='center' cellpadding='10' border='2' bgcolor='lightyellow'>";

   print "<tr>";
   print "<td>TEST SEQUENCES";
   print "</td>";

   print "<td>CAP 1";
   print "</td>";
   print "<td>CAP 2";
   print "</td>";
   print "<td>CAP 3";
   print "</td>";
   print "<td>CAP 4";
   print "</td>";
   print "<td>CAP 5";
   print "</td>";
   print "<td>CAP 6";
   print "</td>";



   print "</tr>";


   print "<tr>";
   print "<td>Red LED ON When Circuit breaker OFF?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'c1_red_on',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     

   print "</td>";


   print "<td>";
   print radio_group(-name=>'c2_red_on',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";
 
   print "<td>";
   print radio_group(-name=>'c3_red_on',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>";
   print radio_group(-name=>'c4_red_on',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>";
   print radio_group(-name=>'c5_red_on',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>";
   print radio_group(-name=>'c6_red_on',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

 

  print "</tr>";


   print "<tr>";
   print "<td>Red LED OFF When Circuit breaker ON?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'c1_red_off',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     

   print "</td>";


   print "<td>";
   print radio_group(-name=>'c2_red_off',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";
 
   print "<td>";
   print radio_group(-name=>'c3_red_off',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>";
   print radio_group(-name=>'c4_red_off',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>";
   print radio_group(-name=>'c5_red_off',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>";
   print radio_group(-name=>'c6_red_off',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

 

  print "</tr>";


   print "<tr>";
   print "<td>Yellow LED Charge?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'c1_yellow',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     

   print "</td>";


   print "<td>";
   print radio_group(-name=>'c2_yellow',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";
 
   print "<td>";
   print radio_group(-name=>'c3_yellow',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>";
   print radio_group(-name=>'c4_yellow',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>";
   print radio_group(-name=>'c5_yellow',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>";
   print radio_group(-name=>'c6_yellow',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

 

  print "</tr>";



   print "<tr>";
   print "<td>Green LED ON when Relay closes?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'c1_green',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     

   print "</td>";


   print "<td>";
   print radio_group(-name=>'c2_green',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";
 
   print "<td>";
   print radio_group(-name=>'c3_green',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>";
   print radio_group(-name=>'c4_green',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>";
   print radio_group(-name=>'c5_green',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>";
   print radio_group(-name=>'c6_green',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

 

  print "</tr>";

   print "<tr>";
   print "<td>12VDC Verified on Capacitor, Relay and Breaker?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'c1_12',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     

   print "</td>";


   print "<td>";
   print radio_group(-name=>'c2_12',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";
 
   print "<td>";
   print radio_group(-name=>'c3_12',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>";
   print radio_group(-name=>'c4_12',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>";
   print radio_group(-name=>'c5_12',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>";
   print radio_group(-name=>'c6_12',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

 

  print "</tr>";

   print "<tr>";
   print "<td>Verify Discharge when breaker turned OFF?";
   print "</td>";
   print "<td>";
   print radio_group(-name=>'c1_dis',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     

   print "</td>";


   print "<td>";
   print radio_group(-name=>'c2_dis',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";
 
   print "<td>";
   print radio_group(-name=>'c3_dis',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>";
   print radio_group(-name=>'c4_dis',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>";
   print radio_group(-name=>'c5_dis',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";

   print "<td>";
   print radio_group(-name=>'c6_dis',
                     -values=>['Yes', 'No'],
                     -default=>'No',
                     -linebreak=>'1',
                   );     
   print "</td>";


  print "</tr>";


   print "</table>";






   print h2("Save the Capacitor Shelf 6 Voltage measurements in mVs to MySQL: ");



       
   print "<table align='center'>";
   print "<tr>";
   print "<td>Enter the Tester's Name:";
   print "<input type='text' id='names' name='names'>";
   print "</td>";
   print "<td rowspan='9'><img src='cap_shelf3.jpg', width=400, height=400>";
   print "</td>";
   print "</tr>";

   print "<tr>";
   print "<td>Enter the Penguin Order ID:";
   print "<input type='text' name='id'>";
   print "</td>";
   print "</tr>";


   print "<tr>";
   print "<td>Enter Capacitor Shelf Serial Number:";
   print "<input type='text' name='sn'>";
   print "</td>";
   print "</tr>";


   print "<tr>";
   print "<td>Enter Capacitor Shelf Circuit1 measurement in mVs:";
   print "<input type='text' name='c1' size='5'>";
   print "</td>";
   print "</tr>";

   print "<tr>";
   print "<td>Enter Capacitor Shelf Circuit2 measurement in mVs:";
   print "<input type='text' name='c2' size='5'>";
   print "</td>";
   print "</tr>";

   print "<tr>";
   print "<td>Enter Capacitor Shelf Circuit3 measurement in mVs:";
   print "<input type='text' name='c3' size='5'>";
   print "</td>";
   print "</tr>";

   print "<tr>";
   print "<td>Enter Capacitor Shelf Circuit4 measurement in mVs:";
   print "<input type='text' name='c4' size='5'>";
   print "</td>";
   print "</tr>";

   print "<tr>";
   print "<td>Enter Capacitor Shelf Circuit5 measurement in mVs:";
   print "<input type='text' name='c5' size='5'>";
   print "</td>";
   print "</tr>";

   print "<tr>";
   print "<td>Enter Capacitor Shelf Circuit6 measurement in mVs:";
   print "<input type='text' name='c6' size='5'>";
   print "</td>";
   print "</tr>";

   print "</table>";

   print h2("Please enter the number of times the respective Circuit Breaker must be reset to achieve a reading of 9mVDC or less: ");

   print "<table align='center' cellpadding='10'>";
   print "<tr>";
   print "<td>CB1 Resets:";
   print "<input type='text' id='cb1' name='cb1' size='2' value='0'>";
   print "</td>";
   print "<td>CB2 Resets:";
   print "<input type='text' id='cb2' name='cb2' size='2' value='0'>";
   print "</td>";

   print "<td>CB3 Resets:";
   print "<input type='text' id='cb3' name='cb3' size='2' value='0'>";
   print "</td>";
   print "<td>CB4 Resets:";
   print "<input type='text' id='cb4' name='cb4' size='2' value='0'>";
   print "</td>";

   print "<td>CB5 Resets:";
   print "<input type='text' id='cb5' name='cb5' size='2' value='0'>";
   print "</td>";
   print "<td>CB6 Resets:";
   print "<input type='text' id='cb6' name='cb6' size='2' value='0'>";
   print "</td>";

   print "</tr>";
   print "</table>";

   print br(),
         submit('action', 'Submit'),
         end_form,
         hr();
}


sub do_work {

   $count = "";

   $center = param('front_panel_center');
   $handles = param('handles');
   $c1_red_on = param(c1_red_on);
   $c2_red_on = param(c2_red_on);
   $c3_red_on = param(c3_red_on);
   $c4_red_on = param(c4_red_on);
   $c5_red_on = param(c5_red_on);
   $c6_red_on = param(c6_red_on);
   $c1_red_off = param(c1_red_off);
   $c2_red_off = param(c2_red_off);
   $c3_red_off = param(c3_red_off);
   $c4_red_off = param(c4_red_off);
   $c5_red_off = param(c5_red_off);
   $c6_red_off = param(c6_red_off);
   $led_seat = param(led_seat);
   $c1_yellow = param(c1_yellow);
   $c2_yellow = param(c2_yellow);
   $c3_yellow = param(c3_yellow);
   $c4_yellow = param(c4_yellow);
   $c5_yellow = param(c5_yellow);
   $c6_yellow = param(c6_yellow);
   $led_orient = param(led_orient);
   $c1_green = param(c1_green);
   $c2_green = param(c2_green);
   $c3_green = param(c3_green);
   $c4_green = param(c4_green);
   $c5_green = param(c5_green);
   $c6_green = param(c6_green);
   $bnc_cable = param(bnc_cable);
   $c1_12 = param(c1_12);
   $c2_12 = param(c2_12);
   $c3_12 = param(c3_12);
   $c4_12 = param(c4_12);
   $c5_12 = param(c5_12);
   $c6_12 = param(c6_12);
   $discharge_flush = param(discharge_flush);
   $c1_dis = param(c1_dis);
   $c2_dis = param(c2_dis);
   $c3_dis = param(c3_dis);
   $c4_dis = param(c4_dis);
   $c5_dis = param(c5_dis);
   $c6_dis = param(c6_dis);

   $discharge_orient = param(discharge_orient);
   $cb_screws = param(cb_screws);
   $busbar = param(busbar);
   $cb_red = param(cb_red);
   $surface = param(surface);
   $cb_cables = param(cb_cables);
   $gauge6 = param(gauge6);
   $red50 = param(red50);
   $black50 = param(black50);
   $sense = param(sense);
   $green_dot = param(green_dot);
   $neg_discharge = param(neg_discharge);
   $pca = param(pca);
   $fan = param(fan);
   $grouped = param(grouped);

   @data = ();
   push (@data, $center, $handles, $c1_red_on, $c2_red_on, $c3_red_on);
   push (@data, $led_seat, $led_orient, $c4_red_on, $c5_red_on, $c6_red_on);
   push (@data, $c1_red_off, $c2_red_off, $c3_red_off, $c4_red_off, $c5_red_off, $c6_red_off);
   push (@data, $c1_yellow, $c2_yellow, $c3_yellow, $c4_yellow, $c5_yellow, $c6_yellow);
   push (@data, $c1_green, $c2_green, $c3_green, $c4_green, $c5_green, $c6_green);
   push (@data, $bnc_cable, $c1_12, $c2_12, $c3_12, $c4_12, $c5_12, $c6_12);
   push (@data, $discharge_flush, $c1_dis, $c2_dis, $c3_dis, $c4_dis, $c5_dis, $c6_dis);
   push (@data, $discharge_orient, $cb_screws, $busbar, $cb_red, $surface, $cb_cables);
   push (@data, $guage6, $red50, $black50, $sense, $green_dot, $neg_discharge, $pca, $fan, $grouped);


   $names = param('names');
   $id = param('id');
   $sn = param('sn');
   $c1 = param('c1');
   $c2 = param('c2');
   $c3 = param('c3');
   $c4 = param('c4');
   $c5 = param('c5');
   $c6 = param('c6');

   $cb1 = param('cb1');
   $cb2 = param('cb2');
   $cb3 = param('cb3');
   $cb4 = param('cb4');
   $cb5 = param('cb5');
   $cb6 = param('cb6');


print <<EE1;
<script type='text/javascript'>
    document.form1.names.value = "$names"
    document.form1.id.value = "$id"
    document.form1.sn.value = "$sn"
    document.form1.c1.value = "$c1"
    document.form1.c2.value = "$c2"
    document.form1.c3.value = "$c3"
    document.form1.c4.value = "$c4"
    document.form1.c5.value = "$c5"
    document.form1.c6.value = "$c6"

    document.form1.cb1.value = "$cb1"
    document.form1.cb2.value = "$cb2"
    document.form1.cb3.value = "$cb3"
    document.form1.cb4.value = "$cb4"
    document.form1.cb5.value = "$cb5"
    document.form1.cb6.value = "$cb6"
</script>
EE1


   print "<BR>";

   @list = ('names','id','sn','c1','c2','c3','c4','c5','c6');
   foreach (@list) {
         if (length(param($_)) == 0) {
           print "Please enter the Name, Order ID, Serial Number and 6 measurements and retry.";

           exit;
        }
           
   }

=pod
print <<EE;
<script type='text/javascript'>
 
           document.write("<br /><em/>The value in the sn field is:<em>" +
           document.form1.sn.value);

</script>
EE
=cut




   @list = ('c1','c2','c3','c4','c5','c6','cb1','cb2','cb3','cb4','cb5','cb6');
   foreach (@list) {
         if (param($_) !~ /^[\d]+\.?[\d]*$/) {
           print "Please enter Numberic data for the 6 measurements and CB data then retry.";
           exit;
        }
           
   }


   ($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdat) = localtime(time);

   $mon++;
   $year += 1900;

   if (length($mon) == 1) {
       $mon = "0" . $mon;
   }

   if (length($sec) == 1) {
        $sec = "0" . $sec;
   }

   if (length($min) == 1) {
        $min = "0" . $min;
   }

   if (length($hour) == 1) {
        $hour = "0" . $hour;
   }

   if (length($mday) == 1) {
        $mday = "0" . $mday;
   }

   $datetimes=$year . "-" . $mon . "-" . $mday . " " . $hour . ":" . $min . ":" . $sec;
   print "<BR>";
         
   if (($c1 < $TEST) && ($c2 < $TEST) && ($c3 < $TEST) && ($c4 < $TEST) && ($c5 < $TEST) && ($c6 < $TEST)) {
      $result = "PASS";
      
      foreach (@data){
           if ($_ eq "No") {
               $result = "FAIL";              
           }
      } 


   } else {
       $result = "FAIL";
   }

   $dbh = DBI->connect('DBI:mysql:production:127.0.0.1','') or print "\n Can not connect to Database, contact Gary to resolve. " , DBI->errstr;


   my $sth=$dbh->prepare("insert into cap_shelf(Order_ID,Tester,Date_Time,Serial_Number,Assembly_Steps,Assembly_Performed,Test_Sequences,Cap1,Cap2,Cap3,Cap4,Cap5,Cap6,Cap1_mvdc,CB1_Resets,Cap2_mvdc,CB2_Resets,Cap3_mvdc,CB3_Resets,Cap4_mvdc,CB4_Resets,Cap5_mvdc,CB5_Resets,Cap6_mvdc,CB6_Resets,Test_Result)
            values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)");



   $sth->execute($id,$names,$datetimes,$sn,"Front Panel Centered and Properly Oriented?",$center,"Red LED ON When Circuit breaker OFF?",$c1_red_on,$c2_red_on,$c3_red_on,$c4_red_on,$c5_red_on,$c6_red_on,$c1,$cb1,$c2,$cb2,$c3,$cb3,$c4,$cb4,$c5,$cb5,$c6,$cb6,$result);
   $sth->execute($id,$names,$datetimes,$sn,"Front Panel Handles Screwed down tight?",$handles,"Red LED OFF When Circuit breaker ON?",$c1_red_off,$c2_red_off,$c3_red_off,$c4_red_off,$c5_red_off,$c6_red_off,"","","","","","","","","","","","","");
   $sth->execute($id,$names,$datetimes,$sn,"LED's Seated Properly onto Holder & Ring?",$led_seat,"Yellow LED Charge?",$c1_yellow,$c2_yellow,$c3_yellow,$c4_yellow,$c5_yellow,$c6_yellow,"","","","","","","","","","","","","");
   $sth->execute($id,$names,$datetimes,$sn,"LED's Oriented Correctly- Top to Bottom(Green/Yellow/Red)?",$led_orient,"Green LED ON when Relay closes?",$c1_green,$c2_green,$c3_green,$c4_green,$c5_green,$c6_green,"","","","","","","","","","","","","");
   $sth->execute($id,$names,$datetimes,$sn,"BNC Cable Properly Installed and Screws Tightened?",$bnc_cable,"12VDC Verified on Capacitor, Relay and Breaker?",$c1_12,$c2_12,$c3_12,$c4_12,$c5_12,$c6_12,"","","","","","","","","","","","","");
   $sth->execute($id,$names,$datetimes,$sn,"Discharge Flush Switch Installed?",$discharge_flush,"Verify Discharge when breaker turned OFF?",$c1_dis,$c2_dis,$c3_dis,$c4_dis,$c5_dis,$c6_dis,"","","","","","","","","","","","","");
   $sth->execute($id,$names,$datetimes,$sn,"Discharge in Correct Orientation and Cables Installed?",$discharge_orient,"","","","","","","","","","","","","","","","","","","","");
   $sth->execute($id,$names,$datetimes,$sn,"M3 Screws on Circuit Breakers Tightened?",$cb_screws,"","","","","","","","","","","","","","","","","","","","");
   $sth->execute($id,$names,$datetimes,$sn,"M3 Screws on BusBar Clips Tightened?",$busbar,"","","","","","","","","","","","","","","","","","","","");
   $sth->execute($id,$names,$datetimes,$sn,"12V Cable (RED) Installed onto Breaker with Split Washer locked?",$cb_red,"","","","","","","","","","","","","","","","","","","","");
   $sth->execute($id,$names,$datetimes,$sn,"12V Cable (RED) Below Surface Wiring?",$surface,"","","","","","","","","","","","","","","","","","","","");
   $sth->execute($id,$names,$datetimes,$sn,"12V Cable (RED) Installed onto Correct Circuit Breaker (1 For 1)?",$cb_cables,"","","","","","","","","","","","","","","","","","","","");
   $sth->execute($id,$names,$datetimes,$sn,"6 Gauge Cable From Breaker to Capacitor * Nut Tightened * ?",$gauge6,"","","","","","","","","","","","","","","","","","","","");
   $sth->execute($id,$names,$datetimes,$sn,"Positive Cable (RED) on Capacitor using M6 Screw + Split/Flat Torque 50?",$red50,"","","","","","","","","","","","","","","","","","","","");
   $sth->execute($id,$names,$datetimes,$sn,"Negative Cable (BLACK) on Capacitor using M6 Screw + Split/Flat Torque 50?",$black50,"","","","","","","","","","","","","","","","","","","","");
   $sth->execute($id,$names,$datetimes,$sn,"Current Sense Ring Cable placed onto Negative Cable (BLACK) cable connected to Capacitor?",$sense,"","","","","","","","","","","","","","","","","","","","");
   $sth->execute($id,$names,$datetimes,$sn,"Current Sense Ring Cable (Green Dot facing away from Capacitor)?",$green_dot,"","","","","","","","","","","","","","","","","","","","");
   $sth->execute($id,$names,$datetimes,$sn,"Negative Discharge Cable (BLACK) Installed in All Capacitors?",$neg_discharge,"","","","","","","","","","","","","","","","","","","","");
   $sth->execute($id,$names,$datetimes,$sn,"PCA Board * Correct Cable Placed Onto Correct Channel * ?",$pca,"","","","","","","","","","","","","","","","","","","","");
   $sth->execute($id,$names,$datetimes,$sn,"12V Fan Cable on PCA Board No. 3 & 4?",$fan,"","","","","","","","","","","","","","","","","","","","");
   $sth->execute($id,$names,$datetimes,$sn,"Cables Properly Grouped and Tie Wrapped * away from risk of damage * ?",$grouped,"","","","","","","","","","","","","","","","","","","","");






   my $sth=$dbh->prepare("select * from cap_shelf
                              where Order_Id = ? and Date_Time = ? and Serial_Number = ?");

   $sth->execute($id,$datetimes,$sn);

#print header, start_html(-title=>"Sample Database", -BGCOLOR=>"#66ff33");

   print "<div align='center'>";
   print h2("Contents of the Capacitor Shelf MySQL measurement data in mVs");
   print qq/<table border="1" cellpadding="10" bgcolor="white">/;

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

#               $data{$val[3]} = $val[0];
#               $time->{"$val[3]"}->{"$val[0]"} = $val[2];
#               $timer->{'3'}->{'5'}='6';
                 $timer->{$val[2]}->{$val[0]}=$val[3];


    }

    print "</table>";
    print "<BR>";
    print "<BR>";

=pod
   print h2("Contents of the Hash:");
   print %data;

   print h2("Contents of the Hash of Hash:");
   print %timer;

foreach $key (keys %{$timer}){
#   print "New Outer key: $key \n";
   while (( $nkey,$nvalue)=each(%{$timer->{$key}})){
      printf "\t Outer key: %s Inner key: %-5s -- Value: %-8s\n", $key, $nkey, $nvalue;
   } 
}

=cut


#print end_html();

    $sth->finish();
    $dbh->disconnect();


}







