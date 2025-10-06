#!D:/xampp/perl/bin/perl.exe
=begin
    our poet template is:
        noun + verb + adv
        noun + adj + verb
=cut
use strict;
use warnings;
sub get_elements{
    my ($filename) = @_;
    my $string = do {
        open(my $fh, '<:encoding(UTF-8)', $filename.'.txt') or die $!;
        local $/;
        <$fh>;
    };
    my @elements = split(/\s*,\s*/, $string);
    return @elements;
}
sub randomer{
    my @arr=@_;
    return @arr[int(rand(@arr))]
}
print "Content-type: text/html\n\n";
print "<html dir=\"rtl\"><head><meta charset='UTF-8'></head><body style='text-align:center;'><h1>شعر را با پرل بخوان:</h1></body></html>";

my @nouns=get_elements("nouns");
my @verbs=get_elements("verbs");
my @adjectives=get_elements("adjectives");
my @adverbs=get_elements("adverbs");
my @places=get_elements("places");

my $random_noun = randomer(@nouns);
my $random_noun_2 = randomer(@nouns);
my $random_verb = randomer(@verbs);
my $random_verb_2 = randomer(@verbs);
my $random_adjective = randomer(@adjectives);
my $random_adverb = randomer(@adverbs);
my $random_place = randomer(@places);

my $beyt1=$random_noun." ".$random_verb." ".$random_place." ".$random_adverb;
my $beyt2=$random_noun_2." ".$random_adjective." ".$random_verb_2;

print "<h2>".$beyt1."&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;".$beyt2."</h2>";