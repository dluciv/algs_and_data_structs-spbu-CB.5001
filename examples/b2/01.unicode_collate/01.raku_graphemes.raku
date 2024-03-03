#!/usr/bin/env raku

say "Сodepoint и графемы";
my $настоящая = "ё";
my $сборная = "е\x[0308]";
my $ненастоящая = "щ\x[0308]";

say "Настоящая: <{$настоящая}>, сборная: <{$сборная}> и ненастоящая: <{$ненастоящая}>";
say "Их длины в графемах: {$настоящая.chars}, {$сборная.chars} и {$ненастоящая.chars}";
say "Их длины в codepoint: {$настоящая.codes}, {$сборная.codes} и {$ненастоящая.codes}";
say "Настоящая и сборная равны? <{$настоящая eq $сборная}>";

say "----------------";
say "Упорядочивание";
# https://docs.raku.org/routine/collate
my $s1 = "coté";
my $s2 = "côte";

# https://dev.to/bbkr/utf-8-sorting-and-collation-p35
# language пока не поддерживается
$*COLLATION.set(
  :primary(True), :secondary(True),
  :tertiary(True), :quaternary(True),
  :language("fr_CA")
);
say ($s1, $s2).collate;
