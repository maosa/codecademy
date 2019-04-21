##### MYSTERY FRIEND PROJECT

"""
You’ve received an anonymous postcard from a friend who you haven’t seen in years. Your friend did not leave a name, but the card is definitely addressed to you. So far, you’ve narrowed your search down to three friends, based on handwriting:

Emma Goldman
Matthew Henson
TingFang Wu

But which one sent you the card?

Just like you can classify a message as spam or not spam with a spam filter, you can classify writing as related to one friend or another by building a kind of friend writing classifier. You have past writing from all three friends stored up in the variable friends_docs, which means you can use scikit-learn’s bag-of-words and Naive Bayes classifier to determine who the mystery friend is!
"""

goldman_raw = """
The history of human growth and development is at the same time the
history of the terrible struggle of every new idea heralding the
approach of a brighter dawn.  In its tenacious hold on tradition, the
Old has never hesitated to make use of the foulest and cruelest means
to stay the advent of the New, in whatever form or period the latter
may have asserted itself.  Nor need we retrace our steps into the
distant past to realize the enormity of opposition, difficulties, and
hardships placed in the path of every progressive idea.  The rack,
the thumbscrew, and the knout are still with us; so are the convict's
garb and the social wrath, all conspiring against the spirit that is
serenely marching on.

Anarchism could not hope to escape the fate of all other ideas of
innovation.  Indeed, as the most revolutionary and uncompromising
innovator, Anarchism must needs meet with the combined ignorance and
venom of the world it aims to reconstruct.

To deal even remotely with all that is being said and done against
Anarchism would necessitate the writing of a whole volume.  I shall
therefore meet only two of the principal objections.  In so doing, I
shall attempt to elucidate what Anarchism really stands for.

The strange phenomenon of the opposition to Anarchism is that it
brings to light the relation between so-called intelligence and
ignorance.  And yet this is not so very strange when we consider the
relativity of all things.  The ignorant mass has in its favor that it
makes no pretense of knowledge or tolerance.  Acting, as it always
does, by mere impulse, its reasons are like those of a child.
"Why?"  "Because."  Yet the opposition of the uneducated to Anarchism
deserves the same consideration as that of the intelligent man.

What, then, are the objections?  First, Anarchism is impractical,
though a beautiful ideal.  Second, Anarchism stands for violence and
destruction, hence it must be repudiated as vile and dangerous.
Both the intelligent man and the ignorant mass judge not from a
thorough knowledge of the subject, but either from hearsay or false
interpretation.

A practical scheme, says Oscar Wilde, is either one already in
existence, or a scheme that could be carried out under the existing
conditions; but it is exactly the existing conditions that one
objects to, and any scheme that could accept these conditions is
wrong and foolish.  The true criterion of the practical, therefore,
is not whether the latter can keep intact the wrong or foolish;
rather is it whether the scheme has vitality enough to leave the
stagnant waters of the old, and build, as well as sustain, new life.
In the light of this conception, Anarchism is indeed practical.
More than any other idea, it is helping to do away with the wrong and
foolish; more than any other idea, it is building and sustaining new
life.

The emotions of the ignorant man are continuously kept at a pitch by
the most blood-curdling stories about Anarchism.  Not a thing too
outrageous to be employed against this philosophy and its exponents.
Therefore Anarchism represents to the unthinking what the proverbial
bad man does to the child,--a black monster bent on swallowing
everything; in short, destruction and violence.

Destruction and violence!  How is the ordinary man to know that the
most violent element in society is ignorance; that its power of
destruction is the very thing Anarchism is combating?  Nor is he
aware that Anarchism, whose roots, as it were, are part of nature's
forces, destroys, not healthful tissue, but parasitic growths that
feed on the life's essence of society.  It is merely clearing the
soil from weeds and sagebrush, that it may eventually bear healthy
fruit.

Someone has said that it requires less mental effort to condemn than
to think.  The widespread mental indolence, so prevalent in society,
proves this to be only too true.  Rather than to go to the bottom of
any given idea, to examine into its origin and meaning, most people
will either condemn it altogether, or rely on some superficial or
prejudicial definition of non-essentials.

Anarchism urges man to think, to investigate, to analyze every
proposition; but that the brain capacity of the average reader be not
taxed too much, I also shall begin with a definition, and then
elaborate on the latter.

     ANARCHISM:--The philosophy of a new social order based on
       liberty unrestricted by man-made law; the theory that all
       forms of government rest on violence, and are therefore wrong
       and harmful, as well as unnecessary.

The new social order rests, of course, on the materialistic basis of
life; but while all Anarchists agree that the main evil today is an
economic one, they maintain that the solution of that evil can be
brought about only through the consideration of EVERY PHASE of
life,--individual, as well as the collective; the internal, as well
as the external phases.

A thorough perusal of the history of human development will disclose
two elements in bitter conflict with each other; elements that are
only now beginning to be understood, not as foreign to each other,
but as closely related and truly harmonious, if only placed in proper
environment: the individual and social instincts.  The individual and
society have waged a relentless and bloody battle for ages, each
striving for supremacy, because each was blind to the value and
importance of the other.  The individual and social instincts,--the
one a most potent factor for individual endeavor, for growth,
aspiration, self-realization; the other an equally potent factor for
mutual helpfulness and social well-being.

The explanation of the storm raging within the individual, and
between him and his surroundings, is not far to seek.  The primitive
man, unable to understand his being, much less the unity of all life,
felt himself absolutely dependent on blind, hidden forces ever ready
to mock and taunt him.  Out of that attitude grew the religious
concepts of man as a mere speck of dust dependent on superior powers
on high, who can only be appeased by complete surrender.  All the
early sagas rest on that idea, which continues to be the LEIT-MOTIF
of the biblical tales dealing with the relation of man to God, to the
State, to society.  Again and again the same motif, MAN IS NOTHING,
THE POWERS ARE EVERYTHING.  Thus Jehovah would only endure man on
condition of complete surrender.  Man can have all the glories of the
earth, but he must not become conscious of himself.  The State,
society, and moral laws all sing the same refrain: Man can have all
the glories of the earth, but he must not become conscious of
himself.

Anarchism is the only philosophy which brings to man the
consciousness of himself; which maintains that God, the State, and
society are non-existent, that their promises are null and void,
since they can be fulfilled only through man's subordination.
Anarchism is therefore the teacher of the unity of life; not merely
in nature, but in man.  There is no conflict between the individual
and the social instincts, any more than there is between the heart
and the lungs: the one the receptacle of a precious life essence, the
other the repository of the element that keeps the essence pure and
strong.  The individual is the heart of society, conserving the
essence of social life; society is the lungs which are distributing
the element to keep the life essence--that is, the individual--pure
and strong.

"The one thing of value in the world," says Emerson, "is the active
soul; this every man contains within him.  The soul active sees
absolute truth and utters truth and creates."  In other words, the
individual instinct is the thing of value in the world.  It is the
true soul that sees and creates the truth alive, out of which is to
come a still greater truth, the re-born social soul.

Anarchism is the great liberator of man from the phantoms that have
held him captive; it is the arbiter and pacifier of the two forces
for individual and social harmony.  To accomplish that unity,
Anarchism has declared war on the pernicious influences which have so
far prevented the harmonious blending of individual and social
instincts, the individual and society.

Religion, the dominion of the human mind; Property, the dominion of
human needs; and Government, the dominion of human conduct, represent
the stronghold of man's enslavement and all the horrors it entails.
Religion! How it dominates man's mind, how it humiliates and degrades
his soul.  God is everything, man is nothing, says religion.  But out
of that nothing God has created a kingdom so despotic, so tyrannical,
so cruel, so terribly exacting that naught but gloom and tears and
blood have ruled the world since gods began.  Anarchism rouses man to
rebellion against this black monster.  Break your mental fetters, says
Anarchism to man, for not until you think and judge for yourself will
you get rid of the dominion of darkness, the greatest obstacle to all
progress.

Property, the dominion of man's needs, the denial of the right to
satisfy his needs.  Time was when property claimed a divine right,
when it came to man with the same refrain, even as religion,
"Sacrifice! Abnegate! Submit!"  The spirit of Anarchism has lifted
man from his prostrate position.  He now stands erect, with his face
toward the light.  He has learned to see the insatiable, devouring,
devastating nature of property, and he is preparing to strike the
monster dead.

"Property is robbery," said the great French Anarchist, Proudhon.
Yes, but without risk and danger to the robber.  Monopolizing the
accumulated efforts of man, property has robbed him of his
birthright, and has turned him loose a pauper and an outcast.
Property has not even the time-worn excuse that man does not create
enough to satisfy all needs.  The A B C student of economics knows
that the productivity of labor within the last few decades far
exceeds normal demand a hundredfold.  But what are normal demands to
an abnormal institution?  The only demand that property recognizes is
its own gluttonous appetite for greater wealth, because wealth means
power; the power to subdue, to crush, to exploit, the power to
enslave, to outrage, to degrade.  America is particularly boastful of
her great power, her enormous national wealth.  Poor America, of what
avail is all her wealth, if the individuals comprising the nation are
wretchedly poor?  If they live in squalor, in filth, in crime, with
hope and joy gone, a homeless, soilless army of human prey.

It is generally conceded that unless the returns of any business
venture exceed the cost, bankruptcy is inevitable.  But those engaged
in the business of producing wealth have not yet learned even this
simple lesson.  Every year the cost of production in human life is
growing larger (50,000 killed, 100,000 wounded in America last year);
the returns to the masses, who help to create wealth, are ever
getting smaller.  Yet America continues to be blind to the inevitable
bankruptcy of our business of production.  Nor is this the only crime
of the latter.  Still more fatal is the crime of turning the producer
into a mere particle of a machine, with less will and decision than
his master of steel and iron.  Man is being robbed not merely of the
products of his labor, but of the power of free initiative, of
originality, and the interest in, or desire for, the things he is
making.

Real wealth consists in things of utility and beauty, in things that
help to create strong, beautiful bodies and surroundings inspiring to
live in.  But if man is doomed to wind cotton around a spool, or dig
coal, or build roads for thirty years of his life, there can be no
talk of wealth.  What he gives to the world is only gray and hideous
things, reflecting a dull and hideous existence,--too weak to live,
too cowardly to die.  Strange to say, there are people who extol this
deadening method of centralized production as the proudest
achievement of our age.  They fail utterly to realize that if we are
to continue in machine subserviency, our slavery is more complete
than was our bondage to the King.  They do not want to know that
centralization is not only the death-knell of liberty, but also of
health and beauty, of art and science, all these being impossible in
a clock-like, mechanical atmosphere.

Anarchism cannot but repudiate such a method of production: its goal
is the freest possible expression of all the latent powers of the
individual.  Oscar Wilde defines a perfect personality as "one who
develops under perfect conditions, who is not wounded, maimed, or in
danger."  A perfect personality, then, is only possible in a state of
society where man is free to choose the mode of work, the conditions
of work, and the freedom to work.  One to whom the making of a table,
the building of a house, or the tilling of the soil, is what the
painting is to the artist and the discovery to the scientist,--the
result of inspiration, of intense longing, and deep interest in work
as a creative force.  That being the ideal of Anarchism, its economic
arrangements must consist of voluntary productive and distributive
associations, gradually developing into free communism, as the best
means of producing with the least waste of human energy.  Anarchism,
however, also recognizes the right of the individual, or numbers of
individuals, to arrange at all times for other forms of work, in
harmony with their tastes and desires.

Such free display of human energy being possible only under complete
individual and social freedom, Anarchism directs its forces against
the third and greatest foe of all social equality; namely, the State,
organized authority, or statutory law,--the dominion of human
conduct.

Just as religion has fettered the human mind, and as property, or the
monopoly of things, has subdued and stifled man's needs, so has the
State enslaved his spirit, dictating every phase of conduct.  "All
government in essence," says Emerson, "is tyranny."  It matters not
whether it is government by divine right or majority rule.  In every
instance its aim is the absolute subordination of the individual.

Referring to the American government, the greatest American
Anarchist, David Thoreau, said: "Government, what is it but a
tradition, though a recent one, endeavoring to transmit itself
unimpaired to posterity, but each instance losing its integrity; it
has not the vitality and force of a single living man.  Law never
made man a whit more just; and by means of their respect for it, even
the well disposed are daily made agents of injustice."

Indeed, the keynote of government is injustice.  With the arrogance
and self-sufficiency of the King who could do no wrong, governments
ordain, judge, condemn, and punish the most insignificant offenses,
while maintaining themselves by the greatest of all offenses, the
annihilation of individual liberty.  Thus Ouida is right when she
maintains that "the State only aims at instilling those qualities in
its public by which its demands are obeyed, and its exchequer is
filled.  Its highest attainment is the reduction of mankind to
clockwork.  In its atmosphere all those finer and more delicate
liberties, which require treatment and spacious expansion, inevitably
dry up and perish.  The State requires a taxpaying machine in which
there is no hitch, an exchequer in which there is never a deficit,
and a public, monotonous, obedient, colorless, spiritless, moving
humbly like a flock of sheep along a straight high road between two
walls."

Yet even a flock of sheep would resist the chicanery of the State, if
it were not for the corruptive, tyrannical, and oppressive methods it
employs to serve its purposes.  Therefore Bakunin repudiates the
State as synonymous with the surrender of the liberty of the
individual or small minorities,--the destruction of social
relationship, the curtailment, or complete denial even, of life
itself, for its own aggrandizement.  The State is the altar of
political freedom and, like the religious altar, it is maintained for
the purpose of human sacrifice.

The average man with his self-sufficiency, his ridiculously superior
airs of patronage towards the female sex, is an impossibility for
woman as depicted in the CHARACTER STUDY by Laura Marholm.  Equally
impossible for her is the man who can see in her nothing more than
her mentality and her genius, and who fails to awaken her woman
nature.

A rich intellect and a fine soul are usually considered necessary
attributes of a deep and beautiful personality.  In the case of the
modern woman, these attributes serve as a hindrance to the complete
assertion of her being.  For over a hundred years the old form of
marriage, based on the Bible, "till death doth part," has been
denounced as an institution that stands for the sovereignty of the
man over the woman, of her complete submission to his whims and
commands, and absolute dependence on his name and support.  Time and
again it has been conclusively proved that the old matrimonial
relation restricted woman to the function of a man's servant and the
bearer of his children.  And yet we find many emancipated women who
prefer marriage, with all its deficiencies, to the narrowness of an
unmarried life; narrow and unendurable because of the chains of moral
and social prejudice that cramp and bind her nature.

The explanation of such inconsistency on the part of many advanced
women is to be found in the fact that they never truly understood the
meaning of emancipation.  They thought that all that was needed was
independence from external tyrannies; the internal tyrants, far more
harmful to life and growth--ethical and social conventions--were left
to take care of themselves; and they have taken care of themselves.
They seem to get along as beautifully in the heads and hearts of the
most active exponents of woman's emancipation, as in the heads and
hearts of our grandmothers.

These internal tyrants, whether they be in the form of public opinion
or what will mother say, or brother, father, aunt, or relative of any
sort; what will Mrs. Grundy, Mr. Comstock, the employer, the Board of
Education say?  All these busybodies, moral detectives, jailers of
the human spirit, what will they say?  Until woman has learned to
defy them all, to stand firmly on her own ground and to insist upon
her own unrestricted freedom, to listen to the voice of her nature,
whether it call for life's greatest treasure, love for a man, or her
most glorious privilege, the right to give birth to a child, she
cannot call herself emancipated.  How many emancipated women are
brave enough to acknowledge that the voice of love is calling, wildly
beating against their breasts, demanding to be heard, to be
satisfied.

The French writer, Jean Reibrach, in one of his novels, NEW BEAUTY,
attempts to picture the ideal, beautiful, emancipated woman.  This
ideal is embodied in a young girl, a physician.  She talks very
cleverly and wisely of how to feed infants; she is kind, and
administers medicines free to poor mothers.  She converses with a
young man of her acquaintance about the sanitary conditions of the
future, and how various bacilli and germs shall be exterminated by
the use of stone walls and floors, and by the doing away with rugs
and hangings.  She is, of course, very plainly and practically
dressed, mostly in black.  The young man, who, at their first
meeting, was overawed by the wisdom of his emancipated friend,
gradually learns to understand her, and recognizes one fine day that
he loves her.  They are young, and she is kind and beautiful, and
though always in rigid attire, her appearance is softened by a
spotlessly clean white collar and cuffs.  One would expect that he
would tell her of his love, but he is not one to commit romantic
absurdities.  Poetry and the enthusiasm of love cover their blushing
faces before the pure beauty of the lady.  He silences the voice of
his nature, and remains correct.  She, too, is always exact, always
rational, always well behaved.  I fear if they had formed a union,
the young man would have risked freezing to death.  I must confess
that I can see nothing beautiful in this new beauty, who is as cold
as the stone walls and floors she dreams of.  Rather would I have the
love songs of romantic ages, rather Don Juan and Madame Venus, rather
an elopement by ladder and rope on a moonlight night, followed by the
father's curse, mother's moans, and the moral comments of neighbors,
than correctness and propriety measured by yardsticks.  If love does
not know how to give and take without restrictions, it is not love,
but a transaction that never fails to lay stress on a plus and a
minus.

The greatest shortcoming of the emancipation of the present day lies
in its artificial stiffness and its narrow respectabilities, which
produce an emptiness in woman's soul that will not let her drink from
the fountain of life.  I once remarked that there seemed to be a
deeper relationship between the old-fashioned mother and hostess,
ever on the alert for the happiness of her little ones and the
comfort of those she loved, and the truly new woman, than between
the latter and her average emancipated sister.  The disciples of
emancipation pure and simple declared me a heathen, fit only for the
stake.  Their blind zeal did not let them see that my comparison
between the old and the new was merely to prove that a goodly number
of our grandmothers had more blood in their veins, far more humor and
wit, and certainly a greater amount of naturalness, kind-heartedness,
and simplicity, than the majority of our emancipated professional
women who fill the colleges, halls of learning, and various offices.
This does not mean a wish to return to the past, nor does it condemn
woman to her old sphere, the kitchen and the nursery.

Salvation lies in an energetic march onward towards a brighter and
clearer future.  We are in need of unhampered growth out of old
traditions and habits.  The movement for woman's emancipation has so
far made but the first step in that direction.  It is to be hoped
that it will gather strength to make another.  The right to vote, or
equal civil rights, may be good demands, but true emancipation begins
neither at the polls nor in courts.  It begins in woman's soul.
History tells us that every oppressed class gained true liberation
from its masters through its own efforts.  It is necessary that woman
learn that lesson, that she realize that her freedom will reach as
far as her power to achieve her freedom reaches.  It is, therefore,
far more important for her to begin with her inner regeneration, to
cut loose from the weight of prejudices, traditions, and customs.
The demand for equal rights in every vocation of life is just and
fair; but, after all, the most vital right is the right to love and
be loved.  Indeed, if partial emancipation is to become a complete
and true emancipation of woman, it will have to do away with the
ridiculous notion that to be loved, to be sweetheart and mother, is
synonymous with being slave or subordinate.  It will have to do away
with the absurd notion of the dualism of the sexes, or that man and
woman represent two antagonistic worlds.

Pettiness separates; breadth unites.  Let us be broad and big.  Let
us not overlook vital things because of the bulk of trifles
confronting us.  A true conception of the relation of the sexes will
not admit of conqueror and conquered; it knows of but one great
thing: to give of one's self boundlessly, in order to find one's self
richer, deeper, better.  That alone can fill the emptiness, and
transform the tragedy of woman's emancipation into joy, limitless
joy.

The popular notion about marriage and love is that they are
synonymous, that they spring from the same motives, and cover the
same human needs.  Like most popular notions this also rests not on
actual facts, but on superstition.

Marriage and love have nothing in common; they are as far apart as
the poles; are, in fact, antagonistic to each other.  No doubt some
marriages have been the result of love.  Not, however, because love
could assert itself only in marriage; much rather is it because few
people can completely outgrow a convention.  There are today large
numbers of men and women to whom marriage is naught but a farce, but
who submit to it for the sake of public opinion.  At any rate, while
it is true that some marriages are based on love, and while it is
equally true that in some cases love continues in married life, I
maintain that it does so regardless of marriage, and not because of
it.

On the other hand, it is utterly false that love results from
marriage.  On rare occasions one does hear of a miraculous case of a
married couple falling in love after marriage, but on close
examination it will be found that it is a mere adjustment to the
inevitable.  Certainly the growing-used to each other is far away
from the spontaneity, the intensity, and beauty of love, without
which the intimacy of marriage must prove degrading to both the woman
and the man.

Marriage is primarily an economic arrangement, an insurance pact.  It
differs from the ordinary life insurance agreement only in that it is
more binding, more exacting.  Its returns are insignificantly small
compared with the investments.  In taking out an insurance policy one
pays for it in dollars and cents, always at liberty to discontinue
payments.  If, however, woman's premium is her husband, she pays for
it with her name, her privacy, her self-respect, her very life,
"until death doth part."  Moreover, the marriage insurance condemns
her to life-long dependency, to parasitism, to complete uselessness,
individual as well as social.  Man, too, pays his toll, but as his
sphere is wider, marriage does not limit him as much as woman.  He
feels his chains more in an economic sense.

Thus Dante's motto over Inferno applies with equal force to marriage.
"Ye who enter here leave all hope behind."

That marriage is a failure none but the very stupid will deny.  One
has but to glance over the statistics of divorce to realize how
bitter a failure marriage really is.  Nor will the stereotyped
Philistine argument that the laxity of divorce laws and the growing
looseness of woman account for the fact that: first, every twelfth
marriage ends in divorce; second, that since 1870 divorces have
increased from 28 to 73 for every hundred thousand population; third,
that adultery, since 1867, as ground for divorce, has increased 270.8
per cent.; fourth, that desertion increased 369.8 per cent.

Added to these startling figures is a vast amount of material,
dramatic and literary, further elucidating this subject.  Robert
Herrick, in TOGETHER; Pinero, in MID-CHANNEL; Eugene Walter, in PAID
IN FULL, and scores of other writers are discussing the barrenness,
the monotony, the sordidness, the inadequacy of marriage as a factor
for harmony and understanding.

The thoughtful social student will not content himself with the
popular superficial excuse for this phenomenon.  He will have to dig
deeper into the very life of the sexes to know why marriage proves so
disastrous.

Edward Carpenter says that behind every marriage stands the life-long
environment of the two sexes; an environment so different from each
other that man and woman must remain strangers.  Separated by an
insurmountable wall of superstition, custom, and habit, marriage has
not the potentiality of developing knowledge of, and respect for,
each other, without which every union is doomed to failure.

Henrik Ibsen, the hater of all social shams, was probably the first
to realize this great truth.  Nora leaves her husband, not--as the
stupid critic would have it--because she is tired of her
responsibilities or feels the need of woman's rights, but because she
has come to know that for eight years she had lived with a stranger
and borne him children.  Can there be anything more humiliating, more
degrading than a life-long proximity between two strangers?  No need
for the woman to know anything of the man, save his income.  As to
the knowledge of the woman--what is there to know except that she has
a pleasing appearance?  We have not yet outgrown the theologic myth
that woman has no soul, that she is a mere appendix to man, made out
of his rib just for the convenience of the gentleman who was so
strong that he was afraid of his own shadow.

Perchance the poor quality of the material whence woman comes is
responsible for her inferiority.  At any rate, woman has no
soul--what is there to know about her?  Besides, the less soul a
woman has the greater her asset as a wife, the more readily will she
absorb herself in her husband.  It is this slavish acquiescence to
man's superiority that has kept the marriage institution seemingly
intact for so long a period.  Now that woman is coming into her own,
now that she is actually growing aware of herself as being outside
of the master's grace, the sacred institution of marriage is
gradually being undermined, and no amount of sentimental lamentation
can stay it.

From infancy, almost, the average girl is told that marriage is her
ultimate goal; therefore her training and education must be directed
towards that end.  Like the mute beast fattened for slaughter, she is
prepared for that.  Yet, strange to say, she is allowed to know much
less about her function as wife and mother than the ordinary artisan
of his trade.  It is indecent and filthy for a respectable girl to
know anything of the marital relation.  Oh, for the inconsistency of
respectability, that needs the marriage vow to turn something which
is filthy into the purest and most sacred arrangement that none dare
question or criticize.  Yet that is exactly the attitude of the
average upholder of marriage.  The prospective wife and mother is
kept in complete ignorance of her only asset in the competitive
field--sex.  Thus she enters into life-long relations with a man only
to find herself shocked, repelled, outraged beyond measure by the
most natural and healthy instinct, sex.  It is safe to say that a
large percentage of the unhappiness, misery, distress, and physical
suffering of matrimony is due to the criminal ignorance in sex
matters that is being extolled as a great virtue.  Nor is it at all
an exaggeration when I say that more than one home has been broken up
because of this deplorable fact.


If, however, woman is free and big enough to learn the mystery of sex
without the sanction of State or Church, she will stand condemned as
utterly unfit to become the wife of a "good" man, his goodness
consisting of an empty brain and plenty of money.  Can there be
anything more outrageous than the idea that a healthy, grown woman,
full of life and passion, must deny nature's demand, must subdue her
most intense craving, undermine her health and break her spirit, must
stunt her vision, abstain from the depth and glory of sex experience
until a "good" man comes along to take her unto himself as a wife?
That is precisely what marriage means.  How can such an arrangement
end except in failure?  This is one, though not the least important,
factor of marriage, which differentiates it from love.

Ours is a practical age.  The time when Romeo and Juliet risked the
wrath of their fathers for love, when Gretchen exposed herself to the
gossip of her neighbors for love, is no more.  If, on rare occasions,
young people allow themselves the luxury of romance, they are taken
in care by the elders, drilled and pounded until they become
"sensible."

The moral lesson instilled in the girl is not whether the man has
aroused her love, but rather is it, "How much?"  The important and
only God of practical American life: Can the man make a living? can
he support a wife?  That is the only thing that justifies marriage.
Gradually this saturates every thought of the girl; her dreams are
not of moonlight and kisses, of laughter and tears; she dreams of
shopping tours and bargain counters.  This soul poverty and
sordidness are the elements inherent in the marriage institution.
The State and Church approve of no other ideal, simply because it is
the one that necessitates the State and Church control of men and
women.

Doubtless there are people who continue to consider love above
dollars and cents.  Particularly this is true of that class whom
economic necessity has forced to become self-supporting.  The
tremendous change in woman's position, wrought by that mighty factor,
is indeed phenomenal when we reflect that it is but a short time
since she has entered the industrial arena.  Six million women wage
workers; six million women, who have equal right with men to be
exploited, to be robbed, to go on strike; aye, to starve even.
Anything more, my lord?  Yes, six million wage workers in every walk
of life, from the highest brain work to the mines and railroad
tracks; yes, even detectives and policemen.  Surely the emancipation
is complete.

Yet with all that, but a very small number of the vast army of women
wage workers look upon work as a permanent issue, in the same light
as does man.  No matter how decrepit the latter, he has been taught
to be independent, self-supporting.  Oh, I know that no one is really
independent in our economic treadmill; still, the poorest specimen of
a man hates to be a parasite; to be known as such, at any rate.

The woman considers her position as worker transitory, to be thrown
aside for the first bidder.  That is why it is infinitely harder to
organize women than men.  "Why should I join a union?  I am going to
get married, to have a home."  Has she not been taught from infancy
to look upon that as her ultimate calling?  She learns soon enough
that the home, though not so large a prison as the factory, has more
solid doors and bars.  It has a keeper so faithful that naught can
escape him.  The most tragic part, however, is that the home no
longer frees her from wage slavery; it only increases her task.
"""

goldman_docs = goldman_raw.split(". ")

henson_raw = """
When the news of the discovery of the North Pole, by Commander Peary,
was first sent to the world, a distinguished citizen of New York City,
well versed in the affairs of the Peary Arctic Club, made the statement,
that he was sure that Matt Henson had been with Commander Peary on the
day of the discovery.

There were not many people who knew who Henson
was, or the reason why the gentleman had made the remark, and, when
asked why he was so certain, he explained that, for the best part of the
twenty years of Commander Peary's Arctic work, his faithful and often
only companion was Matthew Alexander Henson.

To-day there is a more general knowledge of Commander Peary, his work
and his success, and a vague understanding of the fact that Commander
Peary's sole companion from the realm of civilization, when he stood at
the North Pole, was Matthew A. Henson, a Colored Man.

To satisfy the demand of perfectly natural curiosity, I have undertaken
to write a brief autobiography, giving particularly an account of my
Arctic work.

I was born in Charles County, Maryland, August 8, 1866.
The place of my birth was on the Potomac River, about forty-four miles below Washington,
D. C. Slavery days were over forever when I was born. Besides, my
parents were both free born before me, and in my mother's veins ran some
white blood. At an early age, my parents were induced to leave the
country and remove to Washington, D. C. My mother died when I was seven
years old. I was taken in charge by my uncle, who sent me to school, the
"N Street School" in Washington, D. C., which I attended for over six
years. After leaving school I went to Baltimore, Md., where I shipped as
cabin-boy, on board a vessel bound for China. After my first voyage I
became an able-bodied seaman, and for four years followed the sea in
that capacity, sailing to China, Japan, Manilla, North Africa, Spain,
France, and through the Black Sea to Southern Russia.

It was while I was in Washington, D. C., in 1888, that I first attracted
the attention of Commander Peary, who at that time was a civil engineer
in the United States Navy, with the rank of lieutenant, and it was with
the instinct of my race that I recognized in him the qualities that made
me willing to engage myself in his service. I accompanied him as his
body-servant to Nicaragua. I was his messenger at the League Island Navy
Yard, and from the beginning of his second expedition to the Arctic
regions, in 1891, I have been a member of every expedition of his, in
the capacity of assistant: a term that covers a multitude of duties,
abilities, and responsibilities.

The narrative that follows is a record of the last and successful
expedition of the Peary Arctic Club, which had as its attainment the
discovery of the North Pole, and is compiled from notes made by me at
different times during the course of the expedition. I did endeavor to
keep a diary or journal of daily events during my last trip, and did not
find it difficult aboard the ship while sailing north, or when in
winter-quarters at Cape Sheridan, but I found it impossible to make
daily entries while in the field, on account of the constant necessity
of concentrating my attention on the real business of the expedition.
Entries were made daily of the records of temperature and the estimates
of distance traveled; and when solar observations were made the results
were always carefully noted. There were opportunities to complete the
brief entries on several occasions while out on the ice, notably the six
days' enforced delay at the "Big Lead," 84 north, the twelve hours
preceding the return of Captain Bartlett at 87 47' north, and the
thirty-three hours at North Pole, while Commander Peary was determining
to a certainty his position. During the return from the Pole to Cape
Columbia, we were so urged by the knowledge of the supreme necessity of
speed that the thought of recording the events of that part of the
journey did not occur to me so forcibly as to compel me to pay heed to
it, and that story was written aboard the ship while waiting for
favorable conditions to sail toward home lands.

       *       *       *       *       *

It was in June, 1891, that I started on my first trip to the Arctic
regions, as a member of what was known as the "North Greenland
Expedition." Mrs. Peary accompanied her husband, and among the members
of the expedition were Dr. Frederick A. Cook, of Brooklyn, N. Y., Mr.
Langdon Gibson, of Flushing, N. Y., and Mr. Eivind Astrp, of
Christiania, Norway, who had the honor of being the companion of
Commander Peary in the first crossing of North Greenland--and of having
an Esquimo at Cape York become so fond of him that he named his son for
him! It was on this voyage north that Peary's leg was broken.

Mr. John M. Verhoeff, a stalwart young Kentuckian, was also an
enthusiastic member of the party. When the expedition was ready to sail
home the following summer, he lost his life by falling in a crevasse in
a glacier. His body was never recovered. On the first and the last of
Peary's expeditions, success was marred by tragedy. On the last
expedition, Professor Ross G. Marvin, of Cornell University, lost his
life by being drowned in the Arctic Ocean, on his return from his
farthest north, a farther north than had ever been made by any other
explorers except the members of the last expedition. Both Verhoeff and
Marvin were good friends of mine, and I respect and venerate their
memories.

Naturally the impressions formed on my first visit to the Land of Ice
and Snow were the most lasting, but in the coming years I was to learn
more and more that such a life was no picnic, and to realize what
primitive life meant. I was to live with a people who, the scientists
stated, represented the earliest form of human life, living in what is
known as the Stone Age, and I was to revert to that stage of life by
leaps and bounds, and to emerge from it by the same sudden means. Many
and many a time, for periods covering more than twelve months, I have
been to all intents an Esquimo, with Esquimos for companions, speaking
their language, dressing in the same kind of clothes, living in the same
kind of dens, eating the same food, enjoying their pleasures, and
frequently sharing their griefs. I have come to love these people. I
know every man, woman, and child in their tribe. They are my friends and
they regard me as theirs.

After the first return to civilization, I was to come back to the
savage, ice- and rock-bound country seven times more. It was in June,
1893, that I again sailed north with Commander Peary and his party on
board the _Falcon_, a larger ship than the _Kite_, the one we sailed
north in on the previous expedition, and with a much larger equipment,
including several burros from Colorado, which were intended for ice-cap
work, but which did not make good, making better dog-food instead.
Indeed the dogs made life a burden for the poor brutes from the very
start. Mrs. Peary was again a member of the expedition, as well as
another woman, Mrs. Cross, who acted as Mrs. Peary's maid and nurse. It
was on this trip that I adopted the orphan Esquimo boy, Kudlooktoo, his
mother having died just previous to our arrival at the Red Cliffs.
After this boy was washed and scrubbed by me, his long hair cut short,
and his greasy, dirty clothes of skins and furs burned, a new suit made
of odds and ends collected from different wardrobes on the ship made him
a presentable Young American. I was proud of him, and he of me. He
learned to speak English and slept underneath my bunk.

This expedition was larger in numbers than the previous one, but the
results, owing to the impossible weather conditions, were by no means
successful, and the following season all of the expedition returned to
the United States except Commander Peary, Hugh J. Lee, and myself. When
the expedition returned, there were two who went back who had not come
north with us. Miss Marie Ahnighito Peary, aged about ten months, who
first saw the light of day at Anniversary Lodge on the 12th of the
previous September, was taken by her mother to her kinfolks in the
South. Mrs. Peary also took a young Esquimo girl, well known among us as
"Miss Bill," along with her, and kept her for nearly a year, when she
gladly permitted her to return to Greenland and her own people. Miss
Bill is now grown up, and has been married three times and widowed, not
by death but by desertion. She is known as a "Holy Terror." I do not
know the reason why, but I have my suspicions.

The memory of the winter of 1894 and 1895 and the summer following will
never leave me. The events of the journey to 87 6' in 1906 and the
discovery of the North Pole in 1909 are indelibly impressed on my mind,
but the recollections of the long race with death across the 450 miles
of the ice-cap of North Greenland in 1895, with Commander Peary and Hugh
Lee, are still the most vivid.

For weeks and weeks, across the seemingly never-ending wastes of the
ice-cap of North Greenland, I marched with Peary and Lee from
Independence Bay and the land beyond back to Anniversary Lodge. We
started on April 1, 1895, with three sledges and thirty-seven dogs, with
the object of determining to a certainty the northeastern terminus of
Greenland. We reached the northern land beyond the ice-cap, but the
condition of the country did not allow much exploration, and after
killing a few musk-oxen we started on June 1 to make our return. We had
one sledge and nine dogs.

We reached Anniversary Lodge on June 25, with one dog.

The Grim Destroyer had been our constant companion, and it was months
before I fully recovered from the effects of that struggle. When I left
for home and God's Country the following September, on board the good
old _Kite_, it was with the strongest resolution to never again! no
more! forever! leave my happy home in warmer lands.
Nevertheless, the following summer I was again "Northward Bound," with
Commander Peary, to help him secure, and bring to New York, the three
big meteorites that he and Lee had discovered during the winter of
1894-1895.

The meteorites known as "The Woman" and "The Dog" were secured with
comparative ease, and the work of getting the large seventy-ton meteor,
known as "The Tent," into such a position as to insure our securing it
the following summer, was done, so it was not strange that the following
summer I was again in Greenland, but the meteorite was not brought away
that season.

It is well known that the chief characteristic of Commander Peary is
persistency which, coupled with fortitude, is the secret of his success.
The next summer, 1897, he was again at the island after his prize, and
he got it this time and brought it safely to New York, where it now
reposes in the "American Museum of Natural History." As usual I was a
member of the party, and my back still aches when I think of the hard
work I did to help load that monster aboard the _Hope_.

It was during this voyage that Commander Peary announced his
determination to discover the North Pole, and the following years (from
1898 to 1902) were spent in the Arctic.

In 1900, the American record of Farthest North, held by Lockwood and
Brainard, was equaled and exceeded; their cairn visited and their
records removed. On April 21, 1902, a new American record of 84 17' was
made by Commander Peary, further progress north being frustrated by a
lack of provisions and by a lane of open water, more than a mile wide.
This lead or lane of open water I have since become more familiarly
acquainted with. We have called it many names, but it is popularly known
as the "Big Lead." Going north, meeting it can be depended upon. It is
situated just a few miles north of the 84th parallel, and is believed to
mark the continental shelf of the land masses in the Northern
Hemisphere.

During the four years from 1898 to 1902, which were continuously spent
in the regions about North Greenland, we had every experience, except
death, that had ever fallen to the lot of the explorers who had preceded
us, and more than once we looked death squarely in the face. Besides, we
had many experiences that earlier explorers did not meet. In January,
1899, Commander Peary froze his feet so badly that all but one of his
toes fell off.

After the return home, in 1902, it was three years before Commander
Peary made another attack on the Pole, but during those years he was not
resting.

He was preparing to launch his final and "sincerely to be hoped"
successful expedition, and in July, 1905, in the newly built ship,
_Roosevelt_, we were again "Poleward-bound." The following September,
the _Roosevelt_ reached Cape Sheridan, latitude 82 27' north, under her
own steam, a record unequaled by any other vessel, sail or steam.

Early the next year, the negotiation of the Arctic Ocean was commenced,
not as oceans usually are negotiated, but as this ocean must be, by men,
sledges, and dogs. The field party consisted of twenty-six men, twenty
sledges, and one hundred and thirty dogs.

That was an open winter and an early spring, very desirable conditions
in some parts of the world, but very undesirable to us on the northern
coast of Greenland. The ice-pack began disintegrating much too early
that year to suit, but we pushed on, and had it not been for furious
storms enforcing delays and losses of many precious days, the Pole would
have been reached. As it was, Commander Peary and his party got to 87
6' north, thereby breaking _all records_, and in spite of incredible
hardships, hunger and cold, returned safely with all of the expedition,
and on Christmas Eve the _Roosevelt_, after a most trying voyage,
entered New York harbor, somewhat battered but still seaworthy.

Despite the fact that it was to be his last attempt, Commander Peary no
sooner reached home than he announced his intention to return, this time
to be the last, and this time to win.

However, a year intervened, and it was not until July 6, 1908, with the
God-Speed and good wishes of President Roosevelt, that the good ship
named in his honor set sail again. The narrative of that voyage, and the
story of the discovery of the North Pole, follow.

The ages of the wild, misgiving mystery of the North Pole are over,
to-day, and forever it stands under the folds of Old Glory.

July 6, 1908: We're off! For a year and a half I have waited for this
order, and now we have cast off. The shouting and the tumult ceases, the
din of whistles, bells, and throats dies out, and once again the long,
slow surge of the ocean hits the good ship that we have embarked in. It
was at one-thirty P. M. to-day that I saw the last hawse-line cast
adrift, and felt the throb of the engines of our own ship. Chief
Wardwell is on the job, and from now on it is due north.

Oyster Bay, Long Island Sound: We are expecting President Roosevelt. The
ship has been named in his honor and has already made one voyage towards
the North Pole, farther north than any ship has ever made.

July 7: At anchor, the soft wooded hills of Long Island give me a
curious impression. I am waiting for the command to attack the savage
ice- and rock-bound fortress of the North, and here instead we are at
anchor in the neighborhood of sheep grazing in green fields.

Sydney, N. S., July 17, 1908: All of the expedition are aboard and those
going home have gone. Mrs. Peary and the children, Mr. Borup's father,
and Mr. Harry Whitney, and some other guests were the last to leave the
_Roosevelt_, and have given us a last good-by from the tug, which came
alongside to take them off.

Good-by all. Every one is sending back a word to some one he has left
behind, but I have said my good-bys a long time ago, and as I waved my
hand in parting salutation to the little group on the deck of the tug,
my thoughts were with my wife, and I hoped when she next heard of me it
would be with feelings of joy and happiness, and that she would be glad
she had permitted me to leave her for an absence that might never end.

The tenderfeet, as the Commander calls them, are the Doctor, Professor
MacMillan, and young Mr. Borup. The Doctor is a fine-looking, big
fellow, John W. Goodsell, and has a swarthy complexion and straight
hair; on meeting me he told me that he was well acquainted with me by
reputation, and hoped to know me more intimately.

Professor Donald B. MacMillan is a professor in a college in
Massachusetts, near Worcester, and I am going to cultivate his
acquaintance.

Mr. George Borup is the kid, only twenty-one years old but well set up
for his age, always ready to laugh, and has thick, curly hair. I
understand he is a record-breaker in athletics. He will need his
athletic ability on this trip. I am making no judgments or comments on
these fellows now. Wait; I have seen too many enthusiastic starters, and
I am sorry to say some of them did not finish well.

All of the rest of the members of the expedition are the same as were on
the first trip of the _Roosevelt_:--Commander Peary, Captain Bartlett,
Professor Marvin, Chief Engineer Wardwell, Charley Percy the steward,
and myself. The crew has been selected by Captain Bartlett, and are
mostly strangers to me.

Commander Peary is too well known for me to describe him at length;
thick reddish hair turning gray; heavy, bushy eyebrows shading his
"sharpshooter's eyes" of steel gray, and long mustache. His hair grows
rapidly and, when on the march, a thick heavy beard quickly appears. He
is six feet tall, very graceful, and well built, especially about the
chest and shoulders; long arms, and legs slightly bowed. Since losing
his toes, he walks with a peculiar slide-like stride. He has a voice
clear and loud, and words never fail him.

Captain Bartlett is about my height and weight. He has short, curly,
light-brown hair and red cheeks; is slightly round-shouldered, due to
the large shoulder-muscles caused by pulling the oars, and is as quick
in his actions as a cat. His manner and conduct indicate that he has
always been the leader of his crowd from boyhood up, and there is no man
on this ship that he would be afraid to tackle. He is a young man
(thirty-three years old) for a ship captain, but he knows his job.

Professor Marvin is a quiet, earnest person, and has had plenty of
practical experience besides his splendid education. He is rapidly
growing bald; his face is rather thin, and his neck is long. He has
taken great interest in me and, being a teacher, has tried to teach me.
Although I hope to perfect myself in navigation, my knowledge so far
consists only of knot and splice seamanship, and I need to master the
mathematical end.

The Chief Engineer, Mr. Wardwell, is a fine-looking, ruddy-complexioned
giant, with the most honest eyes I have ever looked into. His hair is
thinning and is almost pure white, and I should judge him to be about
forty-five years old. He has the greatest patience, and I have never
seen him lose his temper or get rattled.

Charley Percy is Commander Peary's oldest hand, next to me. He is our
steward, and sees to it that we are properly fed while aboard ship, and
he certainly does see to it with credit to himself.

From Sydney to Hawks Harbor, where we met the _Erik_, has been
uneventful except for the odor of the _Erik_, which is loaded with
whale-meat and can be smelled for miles. We passed St. Paul's Island and
Cape St. George early in the day and through the Straits of Belle Isle
to Hawks Harbor, where there is a whale-factory. From here we leave for
Turnavik.

We have been racing with the _Erik_ all day, and have beaten her to this
place. Captain Bartlett's father owns it, and we loaded a lot of boots
and skins, which the Captain's father had ready for us. From here we
sail to the Esquimo country of North Greenland, without a stop if
possible, as the Commander has no intention of visiting any of the
Danish settlements in South Greenland.

Cape York is our next point, and the ship is sailing free. Aside from
the excitement of the start, and the honor of receiving the personal
visit of the President, and his words of encouragement and cheer, the
trip so far has been uneventful; and I have busied myself in putting my
cabin in order, and making myself useful in overhauling and stowing
provisions in the afterhold.

July 24: Still northward-bound, with the sea rolling and washing over
the ship; and the _Erik_ in the distance seems to be getting her share
of the wash. She is loaded heavily with fresh whale-meat, and is
purposely keeping in leeward of us to spare us the discomfort of the
odor.

July 25 and 26: Busy with my carpenter's kit in the Commander's cabin
and elsewhere. There has been heavy rain and seas, and we have dropped
the _Erik_ completely. The _Roosevelt_ is going fine. We can see the
Greenland coast plainly and to-day, the 29th, we raised and passed Disco
Island. Icebergs on all sides. The light at midnight is almost as bright
as early evening twilight in New York on the Fourth of July and the
ice-blink of the interior ice-cap is quite plain. We have gone through
Baffin's Bay with a rush and raised Duck Island about ten A. M. and
passed and dropped it by two P. M.

I was ashore on Duck Island in 1891, on my first voyage north, and I
remember distinctly the cairn the party built and the money they
deposited in it. I wonder if it is still there? There is little use for
money up here, and the place is seldom visited except by men from the
whalers, when their ships are locked in by ice.

From here it is two hundred miles due north to Cape York.

August 1: Arrived at Cape York Bay and went ashore with the party to
communicate with the Esquimos of whom there were three families. They
remembered us and were dancing up and down the shore, and waving to us
in welcome, and as soon as the bow of the boat had grazed the little
beach, willing hands helped to run her up on shore. These people are
hospitable and helpful, and always willing, sometimes too willing. As an
example, I will tell how, at a settlement farther north, we were going
ashore in one of the whale-boats. Captain Bartlett was forward,
astraddle of the bow with the boat-hook in his hands to fend off the
blocks of ice, and knew perfectly well where he wanted to land, but the
group of excited Esquimos were in his way and though he ordered them
back, they continued running about and getting in his way. In a very
short while the Captain lost patience and commenced to talk loudly and
with excitement; immediately Sipsoo took up his language and parrot-like
started to repeat the Captain's exact words: "Get back there, get
back--how in ---- do you expect me to make a landing?" And thus does the
innocent lamb of the North acquire a civilized tongue.

It is amusing to hear Kudlooktoo in the most charming manner give
Charley a cussing that from any one else would cause Charley to break
his head open.

For the last week I have been busy, with "Matt! The Commander wants
you," "Matt do this," and "Matt do that," and with going ashore and
trading for skins, dogs, lines, and other things; and also
walrus-hunting. I have been up to my neck in work, and have had small
opportunity to keep my diary up to date. We have all put on heavy
clothing; not the regular fur clothes for the winter, but our thickest
civilized clothing, that we would wear in midwinter in the States. In
the middle of the day, if the sun shines, the heat is felt; but if foggy
or cloudy, the heavy clothing is comfortable.

All of the Esquimos want to come aboard and stay aboard. Some we want
and will take along, but there are others we will not have or take along
on a bet, and the pleasant duty of telling them so and putting them
ashore falls to me. It is not a pleasant job to disappoint these people,
but they would be a burden to us and in our way. Besides, we have left
them a plentiful supply of needfuls, and our trading with them has been
fair and generous.

The "Crow's-Nest" has been rigged upon the mainmast, and this morning,
after breakfast, Mr. Whitney, three Esquimos, and myself started in Mr.
Whitney's motor-boat to hunt walrus. The motor gave out very shortly
after the start, and the oars had to be used. We were fortunate in
getting two walrus, which I shot, and then we returned to the ship for
the whale-boat. We left the ship with three more Esquimos in the
whale-boat, and got four more walrus.

Sunday, at Kangerdlooksoah; the land of the reindeer, and the one
pleasant appearing spot on this coast. Mr. Whitney and his six Esquimo
guides have gone hunting for deer, and I have been ashore to trade for
dogs and furs, and have gotten twenty-seven dogs, sealskin-lines for
lashings, a big bearskin, and some foxskins. I try to get furskins from
animals that were killed when in full fur and before they have started
to shed, but some of the skins I have traded in are raw, and will have
to be dried.

I have had the disagreeable job of putting the undesirable ashore, and
it was like handling a lot of sulky school children.

Seegloo, the dog-owner, is invited to bring his pack aboard and is
easily persuaded. He will get a Springfield rifle and loading-outfit and
also a Winchester, if he will sell, and he is more than willing.

And this is the story of day after day from Cape York to Etah Harbor,
which we reached on August 12.
"""

henson_docs = henson_raw.encode('ascii', 'ignore').decode("utf-8").split(". ")

wu_raw = """
The Importance of Names

  "What's in a name?  That which we call a rose
  By any other name would smell as sweet."


Notwithstanding these lines, I maintain that the selection of names is
important.  They should always be carefully chosen.  They are apt to
influence friendships or to excite prejudices according to their
significance.  We Chinese are very particular in this matter.  When a
son is born the father or the grandfather chooses a name for the infant
boy which, according to his horoscope, is likely to insure him success,
or a name is selected which indicates the wish of the family for the
new-born child.  Hence such names as "happiness", "prosperity",
"longevity", "success", and others, with like propitious import, are
common in China.  With regard to girls their names are generally
selected from flowers, fruits, or trees.  Particular care is taken not
to use a name which has a bad meaning.  In Washington I once met a man
in an elevator whose name was "Coffin".  Was I to be blamed for
wondering if the elevator would be my coffin?  On another occasion I
met a man whose name was "Death", and as soon as I heard his name I
felt inclined to run away, for I did not wish to die.  I am not
superstitious.  I have frequently taken dinner with thirteen persons at
the table, and I do not hesitate to start on a journey on a Friday.  I
often do things which would not be done by superstitious persons in
China.  But to meet a man calling himself "Coffin" or "Death" was too
much for me, and with all my disbelief in superstition I could not help
showing some repugnance to those who bore such names.

Equally important, if not more so, is the selection of a name for a
state or a nation.  When the several states of America became
independent they called themselves the "United States of America"--a
very happy idea.  The Union was originally composed of thirteen states,
covering about 300,000 square miles; it is now composed of forty-eight
states and three territories, which in area amount to 3,571,492 square
miles, practically as large in extent as China, the oldest nation in
the world.  It should be noted that the name is most comprehensive:  it
might comprise the entire continent of North and South America.  It is
safe to say that the founders of the nation did not choose such a name
without consideration, and doubtless the designation "United States of
America" conceals a deep motive.  I once asked a gentleman who said he
was an American whether he had come from South or North America, or
whether he was a Mexican, a Peruvian or a native of any of the
countries in Central America?  He replied with emphasis that he was an
American citizen of the United States.  I said it might be the United
States of Mexico, or Argentina, or other United States, but he answered
that when he called himself a citizen it could not mean any other than
that of the United States of America.  I have asked many other
Americans similar questions and they all have given me replies in the
same way.  We Chinese call our nation "The Middle Kingdom"; it was
supposed to be in the center of the earth.  I give credit to the
founders of the United States for a better knowledge of geography than
that possessed by my countrymen of ancient times and do not assume that
the newly formed nation was supposed to comprise the whole continent of
North and South America, yet the name chosen is so comprehensive as to
lead one naturally to suspect that it was intended to include the
entire continent.  However, from my observation of their national
conduct, I believe their purpose was just and humane; it was to set a
noble example to the sister nations in the Western Hemisphere, and to
knit more closely all the nations on that continent through the bonds
of mutual justice, goodwill and friendship.  The American nation is,
indeed, itself a pleasing and unique example of the principle of
democracy.  Its government is ideal, with a liberal constitution, which
in effect declares that all men are created equal, and that the
government is "of the people, for the people, and by the people."
Anyone with ordinary intelligence and with open eyes, who should visit
any city, town or village in America, could not but be impressed with
the orderly and unostentatious way in which it is governed by the local
authorities, or help being struck by the plain and democratic character
of the people.  Even in the elementary schools, democracy is taught and
practised.  I remember visiting a public school for children in
Philadelphia, which I shall never forget.  There were about three or
four hundred children, boys and girls, between seven and fourteen years
of age.  They elected one of their students as mayor, another as judge,
another as police commissioner, and in fact they elected for the
control of their school community almost all the officials who usually
govern a city.  There were a few Chinese children among the students,
and one of them was pointed out to me as the police superintendent.
This not only eloquently spoke of his popularity, but showed goodwill
and harmony among the several hundred children, and the entire absence
of race feeling.  The principals and teachers told me that they had no
difficulty whatever with the students.  If one of them did anything
wrong, which was not often, he would be taken by the student policeman
before the judge, who would try the case, and decide it on its merits,
and punish or discharge his fellow student as justice demanded.  I was
assured by the school authorities that this system of self-government
worked admirably; it not only relieved the teachers of the burden of
constantly looking after the several hundred pupils, but each of them
felt a moral responsibility to behave well, for the sake of preserving
the peace and good name of the school.  Thus early imbued with the idea
of self-government, and entrusted with the responsibilities of its
administration, these children when grown up, take a deep interest in
federal and municipal affairs, and, when elected for office, invariably
perform their duties efficiently and with credit to themselves.

It cannot be disputed that the United States with its democratic system
of government has exercised a great influence over the states and
nations in Central and South America.  The following data showing the
different nations of America, with the dates at which they turned their
respective governments from Monarchies into Republics, all subsequent
to the independence of the United States, are very significant.

Mexico became a Republic in 1823, Honduras in 1839, Salvador in 1839,
Nicaragua in 1821, Costa Rica in 1821, Panama in 1903, Colombia in
1819, Venezuela in 1830, Ecuador in 1810, Brazil in 1889, Peru in 1821,
Bolivia in 1825, Paraguay in 1811, Chile in 1810, Argentina in 1824,
and Uruguay in 1828.

These Republics have been closely modelled upon the republican form of
government of the United States; thus, nearly all the nations or states
on the continent of America have become Republics.  Canada still
belongs to Great Britain.  The fair and generous policy pursued by the
Imperial Government of Great Britain accounts for the Canadians'
satisfaction with their political position, and for the fact that they
do not wish a change.  It must be noted, however, that a section of the
American people would like to see Canada incorporated with the United
States.  I remember that at a public meeting held in Washington, at
which Sir Wilfrid Laurier, then Premier of Canada, was present, an
eminent judge of the Federal Supreme Court jocularly expressed a wish
that Canada should be annexed to the United States.  Later, Mr. Champ
Clark, a leader of the Democratic party in the House of
Representatives, addressed the House urging the annexation of Canada.
Even if these statements are not taken seriously they at least show the
feelings of some people, and he would be a bold man who would prophesy
the political status of Canada in the future.  There is, however, no
present indication of any change being desired by the Canadians, and it
may be safely presumed that the existing conditions will continue for
many years to come.  This is not to be wondered at, for Canada though
nominally a British colony practically enjoys almost all the privileges
of an independent state.  She possesses a constitution similar to that
of the United Kingdom, with a parliament of two houses, called the
"Senate", and the "House of Commons".  The Sovereign of Great Britain
appoints only the Governor General who acts in his name, but the
Dominion is governed by a responsible Ministry, and all domestic
affairs are managed by local officials, without interference from the
Home Government.  Canadians enjoy as many rights as the inhabitants of
England, with the additional advantage that they do not have to bear
the burden of maintaining an army and navy.  Some years ago, if I
remember rightly, in consequence of some agitation or discussion for
independence, the late Lord Derby, then Secretary of State for the
Colonies, stated that if the Canadians really wished for independence,
the Home Government would not oppose, but that they should consider if
they would gain anything by the change, seeing that they already had
self-government, enjoyed all the benefits of a free people, and that
the only right the Home Government reserved was the appointment of the
Governor-General, although it assumed the responsibility of protecting
every inch of their territory from encroachment.  Since this sensible
advice from the Colonial Secretary, I have heard nothing more of the
agitation for independence.

From a commercial point of view, and for the welfare of the people,
there is not much to choose to-day between a Limited Monarchy and a
Republic.  Let us, for instance, compare England with the United
States.  The people of England are as free and independent as the
people of the United States, and though subjects, they enjoy as much
freedom as Americans.  There are, however, some advantages in favor of
a Republic.  Americans until recently paid their President a salary of
only $50,000 a year; it is now $75,000 with an additional allowance of
$25,000 for travelling expenses.  This is small indeed compared with
the Civil List of the King or Emperor of any great nation.  There are
more chances in a Republic for ambitious men to distinguish themselves;
for instance, a citizen can become a president, and practically assume
the functions of a king or an emperor.  In fact the President of the
United States appoints his own cabinet officials, ambassadors,
ministers, etc.  It is generally stated that every new president has
the privilege of making more than ten thousand appointments.  With
regard to the administration and executive functions he has in practice
more power than is usually exercised by a king or an emperor of a
Constitutional Monarchy.  On the other hand, in some matters, the
executive of a Republic cannot do what a king or an emperor can do; for
example, a president cannot declare war against a foreign nation
without first obtaining the consent of Congress.  In a monarchical
government the king or the cabinet officials assume enormous
responsibilities.  Lord Beaconsfield (then Mr. D'Israeli), while he was
Prime Minister of England, purchased in 1875 from the Khedive of Egypt
176,602 Suez Canal shares for the sum of 3,976,582 Pounds on his own
responsibility, and without consulting the Imperial Parliament.  When
Parliament or Congress has to be consulted about everything, great
national opportunities to do some profitable business must undoubtedly
be sometimes lost.  No such bold national investment as that made by
Lord Beaconsfield could have been undertaken by any American president
on his own responsibility.  Mr. Cleveland, when president of the United
States, said that "the public affairs of the United States are
transacted in a glass house."

Washington, in his farewell address, advised his compatriots that on
account of the detached and distant situation of their country they
should, in extending their commercial relations with foreign nations,
have as little political connection with them as possible; and he asked
this pertinent and pregnant question, "Why, by interweaving our destiny
with that of any part of Europe, entangle our peace and prosperity in
the toils of European ambition, rivalship, interest, humor, or
caprice?" In 1823, twenty-seven years after Washington's celebrated
address, President Monroe in his annual message to Congress warned the
European Powers not to plant any new colonies on any portion of the
American hemisphere, as any attempt on their part to extend their
system in that part of the world would be considered as dangerous to
the peace and safety of the United States.  This "Monroe Doctrine", as
it has since been called, practically protects every state and country
on the American continent from attack or interference by any foreign
power, and it cannot be denied that it has been and is now the chief
factor in preserving the integrity of all the countries on that
continent.  Thus the United States is assuming the role of guardian
over the other American nations.  In the city of Washington there is an
International Bureau of the American Republics, in which all the
Republics of Central and South America are represented.  It is housed
in a magnificent palace made possible by the beneficence of Mr. Andrew
Carnegie, the American multi-millionaire and philanthropist, and the
contributions of the different governments.  It cost 750,000 gold
dollars, and Mr. John Barrett, the capable and popular director of the
Bureau, has well called it "a temple of friendship and commerce and a
meeting place for the American Republics."  The Bureau is supported by
the joint contributions of the twenty-one American Republics, and its
affairs are controlled by a governing board composed of their
diplomatic representatives in Washington, with the American Secretary
of State as chairman ex officio.  This institution no doubt strengthens
the position of the United States and is calculated to draw the
American Republics into closer friendship.



Chapter 2.  American Prosperity

One of the main causes of the prosperity of the great American Republic
is its natural resources.  It possesses coal, oil, silver, gold,
copper, and all the other mineral ores.  Nature seems, indeed, to have
provided almost everything that man needs.  The soil is rich; wheat and
every kind of fruit can be grown; but favorable as are these native
conditions they could not be turned to any great advantage without the
skill and industry of enterprising men.  Many countries in Africa and
Asia possess equal advantages, but they are not equally prosperous.
This leads me to the consideration of another reason for America's
growth.  The men who have migrated to the United States have not been
rich people.  They went there to make a living.  They were prepared to
work, their purpose was to improve their condition, and they were
willing to undertake any manual or mental labor to accomplish their
object.  They were hardy and strong and could bear a heavy strain.
Their children inherited their good qualities, and so an American is
generally more hard working and enterprising than most of the people in
Europe and elsewhere.

Another reason for America's success is the great freedom which each
citizen enjoys.  Every man considers himself the equal of every other,
and a young man who is ambitious will not rest until he reaches the top
of his profession or trade.  Thousands of Americans who were once very
poor, have become millionaires or multi-millionaires.  Many of them had
no college education, they taught themselves, and some of them have
become both literary and scholarly.  A college or university education
does not necessarily make a man learned; it only gives him the
opportunity to learn.  It is said that some college men have proven
themselves to be quite ignorant, or rather that they do not know so
much as those who have been self-taught.  I do not in any way wish to
disparage a college education; no doubt men who have been trained in a
university start in life with better prospects and with a greater
chance of success, but those men who have not had such advantages have
doubtless done much to make their country great and prosperous, and
they ought to be recognized as great men.

The general desire of the American people to travel abroad is one of
their good traits.  People who never leave their homes cannot know
much.  A person may become well-informed by reading, but his practical
knowledge cannot be compared with that of a person who has travelled.
We Chinese are great sinners in this regard.  A Chinese maxim says, "It
is dangerous to ride on horseback or to go on a voyage":  hence until
very recently we had a horror of going abroad.  A person who remains
all his life in his own town is generally narrow-minded,
self-opinioned, and selfish.  The American people are free from these
faults.  It is not only the rich and the well-to-do who visit foreign
countries, but tradesmen and workmen when they have saved a little
money also often cross the Atlantic.  Some years ago a Senator in
Washington told me that he crossed the Atlantic Ocean every summer and
spent several months in Europe, and that the next trip would be his
twenty-eighth voyage.  I found, however, that he had never gone beyond
Europe.  I ventured to suggest that he should extend his next annual
journey a little farther and visit Japan, China, and other places in
the Far East which I felt sure he would find both interesting and
instructive.  I have travelled through many countries in Europe and
South America, and wherever I have gone and at whatever hotel I have
put up, I have always found some Americans, and on many occasions I
have met friends and acquaintances whom I had known in Washington or
New York.  But it is not only the men who go abroad; in many cases
ladies also travel by themselves.  On several occasions lady friends
from Washington, Philadelphia, and New York have visited me in Peking.
This is one of the Americans' strong points.  Is it not wiser and much
more useful to disburse a few hundred dollars or so in travelling and
gaining knowledge, coming in contact with other peoples and enlarging
the mind, than to spend large sums of money in gaudy dresses, precious
stones, trinkets, and other luxuries?

In a large country like America where a considerable portion of the
land still remains practically uncultivated or undeveloped, hardy,
industrious, and patient workmen are a necessity.  But the almost
unchecked influx of immigrants who are not desirable citizens cannot
but harm the country.  In these days of international trade it is right
that ingress and egress from one country to another should be
unhampered, but persons who have committed crimes at home, or who are
ignorant and illiterate, cannot become desirable citizens anywhere.
They should be barred out of the United States of America.  It is well
known that foreigners take part in the municipal and federal affairs of
the country as soon as they become citizens.  Now if such persons
really worked for the good of their adopted country, there could be no
objection to this, but it is no secret that many have no such motives.
That being so, it is a question whether steps should not be taken to
limit their freedom.  On the other hand, as many farms suffer from lack
of workmen, people from whatever country who are industrious, patient,
and persevering ought to be admitted as laborers.  They would be a
great boon to the nation.  The fear of competition by cheap labor is
causeless; regulations might be drawn up for the control of these
foreign laborers, and on their arrival they could be drafted to those
places where their services might be most urgently needed.  So long as
honest and steady workmen are excluded for no reason other than that
they are Asiatics, while white men are indiscriminately admitted, I
fear that the prosperity of the country cannot be considered permanent,
for agriculture is the backbone of stable wealth.  Yet at present it is
the country's wealth which is one of the important factors of America's
greatness.  In the United States there are thousands of individuals
whose fortunes are counted by seven or eight figures in gold dollars.
And much of this money has been used to build railways, or to develop
manufactories and other useful industries.  The country has grown great
through useful work, and not on account of the army and navy.  In 1881
America's army numbered only 26,622 men, and her navy consisted of only
24 iron-clads, 2 torpedo-boats, and 25 tugs, but in 1910 the peace
strength of her army was 96,628 and the navy boasted 33 battleships and
120 armored cruisers of different sizes.

Within the last few years it has been the policy of many nations to
increase the army and to build as many Dreadnaughts and
super-dreadnaughts as possible.  Many statesmen have been infected by
this Dreadnaught fever.  Their policy seems to be based on the idea
that the safety of a nation depends on the number of its battleships.
Even peaceful and moderate men are carried away by this hobby, and
support it.  It is forgotten that great changes have taken place during
the last twenty or thirty years; that a nation can now be attacked by
means quite beyond the reach of Dreadnaughts.  The enormous sums spent
on these frightful monsters, if applied to more worthy objects, would
have a greater effect in preserving the nations' heritages than
anything these monstrosities can do.

The nation which has a large army and a strong navy may be called
powerful, but it cannot be considered great without other good
requisites.  I consider a nation as great when she is peacefully,
justly, and humanely governed, and when she possesses a large number of
benevolent and good men who have a voice in the administration.  The
greater the number of good men that a nation possesses the greater she
becomes.  America is known to have a large number of such men and
women, men and women who devote their time and money to preaching peace
among the nations.  Mr. Andrew Carnegie is worth a hundred
Dreadnaughts.  He and others like him are the chief factors in
safeguarding the interests and welfare of America.  The territory of
the United States is separated from Europe and other countries by vast
oceans; so that it would be difficult, if not impossible, for a foe to
successfully attack any portion of that country.  But who wishes to
attack her?  She has scarcely an enemy.  No country is invaded by
another without cause, and as the United States is in friendly
relations with all the Powers, there is no reason to fear foreign
invasion.  Even should a foreign power successfully attack her and
usurp a portion of her territories, a supposition which is most
improbable, would the enemy be able to hold what he seized?  History
shows that no conquered country has ever been successfully and
permanently kept without the people's consent, and there is not the
least chance that the Americans will ever consent to the rule of a
foreign government.

It is to be hoped that the United States will not follow the example of
other nations and unduly increase her armaments, but that she will take
the lead in the universal peace movement and show the world that a
great power can exist and maintain her position without force of arms.
I am aware that general disarmament is not popular among statesmen,
that it has been denounced by an eminent authority as a "will-o'-the
wisp", that arbitration has been styled a "Jack-o'-lantern", but this
is not the first time a good and workable scheme has been branded with
opprobrious names.  The abolition of slavery was at one time considered
to be an insane man's dream; now all people believe in it.  Will the
twentieth century witness the collapse of our present civilization?

Why are the world's armaments constantly increasing?  To my mind it is
due to two causes, one of which is mistrust.  One nation begins to
build Dreadnaughts, another does the same through fear and mistrust.
The second cause is that it is the fashion of some nations to follow
the example of others that they may preserve their position as great
naval powers.  But it is unnecessary for the United States to show such
mistrust or to follow such fashion.  She should rather, as becomes a
great and powerful nation, take an independent course of her own.  If
she sets the example other nations in due time will follow her.  The
peace of the world will be more surely guarded, and America will win
the approbation, the respect, and the gratitude of all peace-loving
people.
It would seem reasonable to expect that in yielding so fully to the
wishes of the United States in this second negotiation the Chinese
Government would not be called upon to make any further concessions in
the interests or at the demand of the labor unions on the Pacific
coast, but in this China was disappointed.  Within a period of less
than ten years an urgent application was made by the American Secretary
of State for a new treaty amended so as to enable the Congress of the
United States to still further restrict the privileges of Chinese
laborers who had come to the United States.  And when the Chinese
Government hesitated to consent to the withdrawal of rights which the
United States granted to the subjects of other Governments, Congress
passed the Scott Act of 1888 prohibiting any Chinese person from
entering the United States except Chinese officials, teachers,
students, merchants or travellers for pleasure or curiosity and
forbidding also Chinese laborers in the United States, after having
left, from returning thereto.  This, in the words of Hon. J. W. Foster,
ex-Secretary of State and a distinguished international lawyer, "was a
deliberate violation of the Treaty of 1880 and was so declared by the
Supreme Court of the United States."  In order to save the Executive of
the United States from embarrassment, the Chinese Government, contrary
to its own sense of justice, and of international comity, for a third
time yielded to the wishes of the United States, and concluded the
amended treaty of 1894 which gave Congress additional power of
legislation respecting Chinese laborers.  By Article I of this treaty
it was agreed that for a term of ten years the coming of Chinese
laborers to the United States should be absolutely prohibited.  Article
III distinctly provided that "the provisions of this convention shall
not affect the right at present enjoyed of Chinese subjects, being
officials, teachers, students, merchants, or travellers for curiosity
or pleasure, but not laborers, of coming to the United States and
residing therein." Thus it is clear that the prohibition affects only
laborers, and not the other classes of Chinese.  For a few years after
the signing of this convention this was the view adopted and acted upon
by the immigration officials, but afterward they changed their
attitude, and the foregoing Article has since been interpreted to mean
that only the above-mentioned five classes can be admitted into the
United States, and that all the other classes of Chinese, however
respectable and honorable, must be refused admission.  Will my readers
believe that a Chinese banker, physician, lawyer, broker, commercial
agent, scholar or professor could all be barred out of the United
States of America under the provisions of this convention?  In the face
of the plain language of the text it seems too absurd and unreasonable
to be contemplated, and yet it is a fact.

This convention was proclaimed in December, 1894.  According to its
provisions, it was to remain in force only for a period of ten years,
but that if six months before the end of that period neither Power
should give notice of denunciation it should be extended for a similar
period.  Such notice was, however, given by China to the United States
and accordingly the convention expired in December, 1904, and is now no
longer in force.  No serious attempt has since been made by the United
States Government to negotiate a new treaty regarding Chinese laborers,
so the customs and immigration officials continue to prohibit Chinese
laborers from coming to America by virtue of the law passed by
Congress.  It will be seen that by the treaty of 1868, known as the
"Burlingame Treaty", the United States Government formally agreed that
Chinese subjects, visiting or residing in the United States, should
enjoy the same privileges and immunities as were enjoyed by the
citizens or subjects of the most favored nation; that being so, and as
the convention of 1894 has expired, according to the legal opinion of
Mr. John W. Foster, and other eminent lawyers, the continuation of the
exclusion of Chinese laborers and the restrictions placed upon Chinese
merchants and others seeking admission to the United States are not
only without international authority but in violation of treaty
stipulations.

The enforcement of the exclusion laws against Chinese in the Hawaiian
and Philippine Islands is still more inexcusable.  The complaint in
America against the immigration of Chinese laborers was that such
immigration was detrimental to white labor, but in those Islands there
has been no such complaint; on the contrary the enforcement of the law
against the Chinese in Hawaii has been, and is, contrary to the
unanimous wish of the local Government and the people.  Free
intercourse and immigration between those Islands and China have been
maintained for centuries.  What is most objectionable and unfair is
that the Chinese should be singled out for discrimination, while all
other Asiatics such as Japanese, Siamese, and Malays are allowed to
enter America and her colonies without restraint.  It is my belief that
the gross injustice that has been inflicted upon the Chinese people by
the harsh working of the exclusion law is not known to the large
majority of the American people, for I am sure they would not allow the
continuation of such hardships to be suffered by those who are their
sincere friends.  China does not wish special treatment, she only asks
that her people shall be treated in the same way as the citizens or
subjects of other countries.  Will the great American nation still
refuse to consent to this?

To solve the problem of immigration in a manner that would be
satisfactory to all parties is not an easy task, as so many conflicting
interests are involved.  But it is not impossible.  If persons
interested in this question be really desirous of seeing it settled and
are willing to listen to reasonable proposals, I believe that a way may
be found for its solution.  There is good reason for my optimistic
opinion.  Even the Labor Unions, unless I am mistaken, would welcome an
amicable settlement of this complicated question.  In 1902, while at
Washington, I was agreeably surprised to receive a deputation of the
leaders of the Central Labor Union of Binghamton, New York, inviting me
to pay a visit there and to deliver an address.  As I did not wish to
disappoint them I accepted their invitation.  During my short stay
there, I was very cordially and warmly received, and most kindly
treated not only by the local authorities and inhabitants, but by the
members of the Labor Union and the working men also.  I found that the
Union leaders and the working men were most reasonable, their platform
being, as far as I could learn, to have no cheap labor competition but
not necessarily discrimination against any race.  If the United States
Government would appoint a commission composed of members representing
the Labor Unions, manufacturers and merchants, to treat with a similar
commission nominated by the Chinese Government, the whole question in
all its bearings could be discussed, and I feel certain that after free
and candid exchange of views, the joint Commissioners would be able to
arrive at a scheme which would put at rest once for all the conflicting
claims, and settle the matter satisfactorily to both China and the
United States.
"""

wu_docs = wu_raw.split(". ")

##### import sklearn modules here:
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

##### Setting up the combined list of friends' writing samples
friends_docs = goldman_docs + henson_docs + wu_docs

##### Setting up labels for your three friends
friends_labels = [1] * 154 + [2] * 141 + [3] * 164

mystery_postcard = """
My friend,
From the 10th of July to the 13th, a fierce storm raged, clouds of
freeing spray broke over the ship, incasing her in a coat of icy mail,
and the tempest forced all of the ice out of the lower end of the
channel and beyond as far as the eye could see, but the _Roosevelt_
still remained surrounded by ice.
Hope to see you soon.
"""

##### Create bow_vectorizer:
bow_vectorizer = CountVectorizer()

##### Define friends_vectors:
friends_vectors = bow_vectorizer.fit_transform(friends_docs)

##### Define mystery_vector:
mystery_vector = bow_vectorizer.transform([mystery_postcard])

##### Lets take a looks at your friends writing samples to get a sense of how they write
##### Print out one document of each friends writing
# print(goldman_docs[40])
# print(henson_docs[80])
# print(wu_docs[120])

##### Define friends_classifier:
friends_classifier = MultinomialNB()

##### Train the classifier:
friends_classifier.fit(friends_vectors, friends_labels)

##### Change predictions:
predictions = friends_classifier.predict(mystery_vector)

mystery_friend = predictions[0] if predictions[0] else "someone else"

print("The postcard was from {}!".format(mystery_friend))
