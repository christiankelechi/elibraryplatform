# from transformers import BartTokenizer, BartForConditionalGeneration

# # Load tokenizer and model
# tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
# model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

# # Function to generate summary
# def generate_summary(text):
#     inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
#     summary_ids = model.generate(inputs, max_length=1000, min_length=300, length_penalty=2.0, num_beams=4, early_stopping=True)
#     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
#     return summary

# # Example text to summarize
# example_text = """From Wikipedia, the free encyclopedia
# This article is about the belief in a supreme being in monotheistic belief systems. For powerful supernatural beings considered divine or sacred, see Deity. For God in specific religions, see Conceptions of God. For other uses, see God (disambiguation).






# Representation (for the purpose of art or worship) of God in (left to right from top) Christianity, Islam, Hinduism, Sikhism, Judaism, and the Baháʼí Faith
# God is usually viewed as the only deity in monotheistic belief systems[1] or the supreme deity or unitary deity in some polytheistic belief systems.[2][3] A deity, or god, is a "spirit or being believed to have created, or for controlling some part of the universe or life, for which such a deity is often worshipped".[4] Belief in the existence of at least one god is called theism.[5]

# Conceptions of God vary considerably. Many notable theologians and philosophers have developed arguments for and against the existence of God.[6] Atheism rejects the belief in any deity. Agnosticism is the belief that the existence of God is unknown or unknowable. Some theists view knowledge concerning God as derived from faith. God is often conceived as the greatest entity in existence.[7] God is often believed to be the cause of all things and so is seen as the creator, sustainer, and ruler of the universe. God is often thought of as incorporeal and independent of the material creation,[7][8][9] while pantheism holds that God is the universe itself. God is sometimes seen as omnibenevolent, while deism holds that God is not involved with humanity apart from creation.

# Some traditions attach spiritual significance to maintaining some form of relationship with God, often involving acts such as worship and prayer, and see God as the source of all moral obligation.[7] God is sometimes described without reference to gender, while others use terminology that is gender-specific. God is referred to by different names depending on the language and cultural tradition, sometimes with different titles of God used in reference to God's various attributes.

# Etymology and usage
# Main article: God (word)

# The Mesha Stele bears the earliest known reference (840 BCE) to the Israelite God Yahweh.
# The earliest written form of the Germanic word God comes from the 6th-century Christian Codex Argenteus. The English word itself is derived from the Proto-Germanic *ǥuđan. The reconstructed Proto-Indo-European form *ǵhu-tó-m was likely based on the root *ǵhau(ə)-, which meant either "to call" or "to invoke".[10] The Germanic words for God were originally neuter, but during the process of the Christianization of the Germanic peoples from their indigenous Germanic paganism, the words became a masculine syntactic form.[11] In the English language, capitalization is used when the word is used as a proper noun, as well as for other names by which a god is known.[12] Consequently, the capitalized form of god is not used for multiple gods or when used to refer to the generic idea of a deity.[13][14]

# The English word God and its counterparts in other languages are normally used for any and all conceptions and, in spite of significant differences between religions, the term remains an English translation common to all.

# El means God in Hebrew, but in Judaism and in Christianity, God is also given a personal name, the tetragrammaton YHWH, in origin possibly the name of an Edomite or Midianite deity, Yahweh.[15] In many English translations of the Bible, when the word LORD is in all capitals, it signifies that the word represents the tetragrammaton.[16] Jah or Yah is an abbreviation of Jahweh/Yahweh, and often sees usage by Jews and Christians in the interjection "Hallelujah", meaning "Praise Jah", which is used to give God glory.[17] In Judaism some of the Hebrew titles of God are considered holy names.

# Allāh (Arabic: الله) is the Arabic term with no plural used by Muslims and Arabic-speaking Christians and Jews meaning "The God", while ʾilāh (Arabic: إِلَٰه plural `āliha آلِهَة) is the term used for a deity or a god in general.[18][19][20] Muslims also use a multitude of other titles for God.

# In Hinduism, Brahman is often considered a monistic concept of God.[21] God may also be given a proper name in monotheistic currents of Hinduism which emphasize the personal nature of God, with early references to his name as Krishna-Vasudeva in Bhagavata or later Vishnu and Hari.[22] Sang Hyang Widhi Wasa is the term used in Balinese Hinduism.[23]

# In Chinese religion, Shangdi is conceived as the progenitor (first ancestor) of the universe, intrinsic to it and constantly bringing order to it.

# Ahura Mazda is the name for God used in Zoroastrianism. "Mazda", or rather the Avestan stem-form Mazdā-, nominative Mazdå, reflects Proto-Iranian *Mazdāh (female). It is generally taken to be the proper name of the spirit, and like its Sanskrit cognate medhā, means "intelligence" or "wisdom". Both the Avestan and Sanskrit words reflect Proto-Indo-Iranian *mazdhā-, from Proto-Indo-European mn̩sdʰeh1, literally meaning "placing (dʰeh1) one's mind (*mn̩-s)", hence "wise".[24] Meanwhile 101 other names are also in use.[25]

# Waheguru (Punjabi: vāhigurū) is a term most often used in Sikhism to refer to God.[26] It means "Wonderful Teacher" in the Punjabi language. Vāhi (a Middle Persian borrowing) means "wonderful" and guru (Sanskrit: guru) is a term denoting "teacher". Waheguru is also described by some as an experience of ecstasy which is beyond all description. The most common usage of the word "Waheguru" is in the greeting Sikhs use with each other – Waheguru Ji Ka Khalsa, Waheguru Ji Ki Fateh "Wonderful Lord's Khalsa, Victory is to the Wonderful Lord."

# Baha, the "greatest" name for God in the Baháʼí Faith, is Arabic for "All-Glorious".[27]

# Other names for God include Aten[28] in ancient Egyptian Atenism where Aten was proclaimed to be the one "true" supreme being and creator of the universe,[29] Chukwu in Igbo,[30] and Hayyi Rabbi in Mandaeism.[31][32]

# General conceptions
# Existence
# Main article: Existence of God
# See also: Theism, Atheism, and Agnosticism

# Thomas Aquinas summed up five main arguments as proofs for God's existence (painting by Carlo Crivelli, 1476).

# Isaac Newton saw the existence of a Creator necessary in the movement of astronomical objects (painting by Godfrey Kneller, 1689).
# The existence of God is a subject of debate in theology, philosophy of religion and popular culture.[33] In philosophical terms, the question of the existence of God involves the disciplines of epistemology (the nature and scope of knowledge) and ontology (study of the nature of being or existence) and the theory of value (since some definitions of God include "perfection").

# Ontological arguments refer to any argument for the existence of God that is based on a priori reasoning.[34] Notable ontological arguments were formulated by Anselm and René Descartes.[35] Cosmological arguments, such as those described below, use concepts around the origin of the universe to argue for the existence of God.

# The Teleological argument, also called the ‘’argument from design’’, uses the complexity within the universe as a proof of the existence of God.[36] It is countered that the fine tuning required for a stable universe with life on earth is illusionary, as humans are only able to observe the small part of this universe that succeeded in making such observation possible, called the anthropic principle, and so would not learn of, for example, life on other planets or of universes that did not occur because of different laws of physics.[37] Non-theists have argued that complex processes that have natural explanations yet to be discovered are referred to the supernatural, called god of the gaps. Other theists, such as John Henry Newman who believed theistic evolution was acceptable, have also argued against versions of the teleological argument and held that it is limiting of God to view him having to only intervene specially in some instances rather than having complex processes designed to create order.[38]

# The Argument from beauty states that this universe happens to contain special beauty in it and that there would be no particular reason for this over aesthetic neutrality other than God.[39] This has been countered by pointing to the existence of ugliness in the universe.[40] This has also been countered by arguing that beauty has no objective reality and so the universe could be seen as ugly or that humans have made what is more beautiful than nature.[41]

# The Argument from morality argues for the existence of God given the assumption of the objective existence of morals.[42] While prominent non-theistic philosophers such as the atheist J. L. Mackie agreed that the argument is valid, they disagreed with its premises. David Hume argued that there is no basis to believe in objective moral truths while biologist E. O. Wilson theorized that the feelings of morality are a by-product of natural selection in humans and would not exist independent of the mind.[43] Philosopher Michael Lou Martin argued that a subjective account for morality can be acceptable. Similar to the argument from morality is the argument from conscience which argues for the existence of God given the existence of a conscience that informs of right and wrong, even against prevailing moral codes. Philosopher John Locke instead argued that conscience is a social construct and thus could lead to contradicting morals.[44]

# Atheism is, in a broad sense, the rejection of belief in the existence of deities.[45][46] Agnosticism is the view that the truth values of certain claims—especially metaphysical and religious claims such as whether God, the divine or the supernatural exist—are unknown and perhaps unknowable.[47][48][49][50] Theism generally holds that God exists objectively and independently of human thought and is sometimes used to refer to any belief in God or gods.[51][52]

# Some view the existence of God as an empirical question. Richard Dawkins states that "a universe with a god would be a completely different kind of universe from one without, and it would be a scientific difference."[53] Carl Sagan argued that the doctrine of a Creator of the Universe was difficult to prove or disprove and that the only conceivable scientific discovery that could disprove the existence of a Creator (not necessarily a God) would be the discovery that the universe is infinitely old.[54] Some theologians, such as Alister McGrath, argue that the existence of God is not a question that can be answered using the scientific method.[55][56]

# Agnostic Stephen Jay Gould argued that science and religion are not in conflict and proposed an approach dividing the world of philosophy into what he called "non-overlapping magisteria" (NOMA).[57] In this view, questions of the supernatural, such as those relating to the existence and nature of God, are non-empirical and are the proper domain of theology. The methods of science should then be used to answer any empirical question about the natural world, and theology should be used to answer questions about ultimate meaning and moral value. In this view, the perceived lack of any empirical footprint from the magisterium of the supernatural onto natural events makes science the sole player in the natural world.[58] Stephen Hawking and co-author Leonard Mlodinow state in their 2010 book, The Grand Design, that it is reasonable to ask who or what created the universe, but if the answer is God, then the question has merely been deflected to that of who created God. Both authors claim, however, that it is possible to answer these questions purely within the realm of science and without invoking divine beings.[59][60]

# Oneness
# Main articles: Deity, Monotheism, and Henotheism

# Trinitarians believe that the Father, the Son, and the Holy Spirit are three distinct persons sharing a single nature or essence.
# A deity, or "god" (with lowercase g), refers to a supernatural being.[61] Monotheism is the belief that there is only one deity, referred to as ‘’God’’ (with uppercase g). Comparing or equating other entities to God is viewed as idolatry in monotheism, and is often strongly condemned. Judaism is one of the oldest monotheistic traditions in the world.[62] Islam's most fundamental concept is tawhid meaning "oneness" or "uniqueness".[63] The first pillar of Islam is an oath that forms the basis of the religion and which non-Muslims wishing to convert must recite, declaring that "I testify that there is no deity except God."[64]

# In Christianity, the doctrine of the Trinity describes God as one God in Father, Son (Jesus), and Holy Spirit.[65] In past centuries, this fundamental mystery of the Christian faith was also summarized by the Latin formula Sancta Trinitas, Unus Deus (Holy Trinity, Unique God), reported in the Litanias Lauretanas.

# God in Hinduism is viewed differently by diverse strands of the religion, with most Hindus having faith in a supreme reality (Brahman) who can be manifested in numerous chosen deities. Thus, the religion is sometimes characterized as Polymorphic Monotheism.[66] Henotheism is the belief and worship of a single god at a time while accepting the validity of worshiping other deities.[67] Monolatry is the belief in a single deity worthy of worship while accepting the existence of other deities.[68]

# Transcendence
# See also: Pantheism and Panentheism
# Transcendence is the aspect of God's nature that is completely independent of the material universe and its physical laws. Many supposed characteristics of God are described in human terms. Anselm thought that God did not feel emotions such as anger or love, but appeared to do so through our imperfect understanding. The incongruity of judging "being" against something that might not exist, led many medieval philosophers approach to knowledge of God through negative attributes, called Negative theology. For example, one should not say that God is wise, but can say that God is not ignorant (i.e. in some way God has some properties of knowledge). Christian theologian Alister McGrath writes that one has to understand a "personal god" as an analogy. "To say that God is like a person is to affirm the divine ability and willingness to relate to others. This does not imply that God is human, or located at a specific point in the universe."[69]

# Pantheism holds that God is the universe and the universe is God and denies that God transcends the Universe.[70] For pantheist philosopher Baruch Spinoza, the whole of the natural universe is made of one substance, God, or its equivalent, Nature.[71][72] Pantheism is sometimes objected to as not providing any meaningful explanation of God with the German philosopher Schopenhauer stating “Pantheism is only a euphemism for atheism”.[73] Pandeism holds that God was a separate entity but then became the Universe.[74][75] Panentheism holds that God contains, but is not identical to, the Universe.[76][77]

# Creator
# See also: Creator deity

# God Blessing the Seventh Day, 1805 watercolor painting by William Blake
# God is often viewed as the cause of all that exists. For Pythagoreans, Monad variously referred to divinity, the first being or an indivisible origin.[78] The philosophy of Plato and Plotinus refers to “The One” which is the first principle of reality that is ‘’beyond’’ being[79] and is both the source of the Universe and the teleological purpose of all things.[80] Aristotle theorized a first uncaused cause for all motion in the universe and viewed it as perfectly beautiful, immaterial, unchanging and indivisible. Aseity is the property of not depending on any cause other than itself for its existence. Avicenna held that there must be a necessarily existent guaranteed to exist by its essence – it cannot ‘’not’’ exist – and that humans identify this as God.[81] Secondary causation refers to God creating the laws of the Universe which then can change themselves within the framework of those laws. In addition to the initial creation, occasionalism refers to the idea that the Universe would not by default continue to exist from one instant to the next and so would need to rely on God as a sustainer. While divine providence refers to any intervention by God, it is usually used to refer to "special providence" where there is an extraordinary intervention by God, such as miracles.[82][83]

# Benevolence
# See also: Deism and Thirteen Attributes of Mercy
# Deism holds that God exists but does not intervene in the world beyond what was necessary to create it,[84] such as answering prayers or producing miracles. Deists sometimes attribute this to God having no interest in or not being aware of humanity. Pandeists would hold that God does not intervene because God is the Universe.[85]

# Of those theists who hold that God has an interest in humanity, most hold that God is omnipotent, omniscient, and benevolent. This belief raises questions about God's responsibility for evil and suffering in the world. Dystheism, which is related to theodicy, is a form of theism which holds that God is either not wholly good or is fully malevolent as a consequence of the problem of evil.

# Omniscience and omnipotence
# Omnipotence (all-powerful) is an attribute often ascribed to God. The omnipotence paradox is most often framed with the example "Could God create a stone so heavy that even he could not lift it?" as God could either be unable to create that stone or lift that stone and so could not be omnipotent. This is often countered with variations of the argument that omnipotence, like any other attribute ascribed to God, only applies as far as it is noble enough to befit God and thus God cannot lie, or do what is contradictory as that would entail opposing himself.[86]

# Omniscience (all-knowing) is an attribute often ascribed to God. This implies that God knows how free agents will choose to act. If God does know this, either their free will might be illusory or foreknowledge does not imply predestination, and if God does not know it, God may not be omniscient.[87] Open Theism limits God's omniscience by contending that, due to the nature of time, God's omniscience does not mean the deity can predict the future and process theology holds that God does not have immutability, so is affected by his creation.

# Other concepts
# Theologians of theistic personalism (the view held by Rene Descartes, Isaac Newton, Alvin Plantinga, Richard Swinburne, William Lane Craig, and most modern evangelicals) argue that God is most generally the ground of all being, immanent in and transcendent over the whole world of reality, with immanence and transcendence being the contrapletes of personality.[88]

# God has also been conceived as being incorporeal (immaterial), a personal being, the source of all moral obligation, and the "greatest conceivable existent".[7] These attributes were all supported to varying degrees by the early Jewish, Christian and Muslim theologian philosophers, including Maimonides,[89] Augustine of Hippo,[89] and Al-Ghazali,[6] respectively.

# Non-theistic views
# Religious traditions
# Jainism has generally rejected creationism, holding that soul substances (Jīva) are uncreated and that time is beginningless.[90]

# Some interpretations and traditions of Buddhism can be conceived as being non-theistic. Buddhism has generally rejected the specific monotheistic view of a Creator God. The Buddha criticizes the theory of creationism in the early Buddhist texts.[91][92] Also, major Indian Buddhist philosophers, such as Nagarjuna, Vasubandhu, Dharmakirti and Buddhaghosa, consistently critiqued Creator God views put forth by Hindu thinkers.[93][94][95] However, as a non-theistic religion, Buddhism leaves the existence of a supreme deity ambiguous. There are significant numbers of Buddhists who believe in God, and there are equally large numbers who deny God's existence or are unsure.[96][97]

# Taoic religions such as Confucianism and Taoism are silent on the existence of creator gods. However, keeping with the tradition of ancestor veneration in China, adherents worship the spirits of people such as Confucius and Lao Tzu in a similar manner to God.[98][99]

# Anthropology
# See also: Evolutionary origin of religions, Evolutionary psychology of religion, and Anthropomorphism
# Some atheists have argued that a single, omniscient God who is imagined to have created the universe and is particularly attentive to the lives of humans has been imagined and embellished over generations.[100]

# Pascal Boyer argues that while there is a wide array of supernatural concepts found around the world, in general, supernatural beings tend to behave much like people. The construction of gods and spirits like persons is one of the best known traits of religion. He cites examples from Greek mythology, which is, in his opinion, more like a modern soap opera than other religious systems.[101]

# Bertrand du Castel and Timothy Jurgensen demonstrate through formalization that Boyer's explanatory model matches physics' epistemology in positing not directly observable entities as intermediaries.[102]

# Anthropologist Stewart Guthrie contends that people project human features onto non-human aspects of the world because it makes those aspects more familiar. Sigmund Freud also suggested that god concepts are projections of one's father.[103]

# Likewise, Émile Durkheim was one of the earliest to suggest that gods represent an extension of human social life to include supernatural beings. In line with this reasoning, psychologist Matt Rossano contends that when humans began living in larger groups, they may have created gods as a means of enforcing morality. In small groups, morality can be enforced by social forces such as gossip or reputation. However, it is much harder to enforce morality using social forces in much larger groups. Rossano indicates that by including ever-watchful gods and spirits, humans discovered an effective strategy for restraining selfishness and building more cooperative groups.[104]

# Neuroscience and psychology
# See also: Jungian interpretation of religion
# Sam Harris has interpreted some findings in neuroscience to argue that God is an imaginary entity only, with no basis in reality.[105]

# Johns Hopkins researchers studying the effects of the “spirit molecule” DMT, which is both an endogenous molecule in the human brain and the active molecule in the psychedelic ayahuasca, found that a large majority of respondents said DMT brought them into contact with a "conscious, intelligent, benevolent, and sacred entity," and describe interactions that oozed joy, trust, love, and kindness. More than half of those who had previously self-identified as atheists described some type of belief in a higher power or God after the experience.[106]

# About a quarter of those afflicted by temporal lobe seizures experience what is described as a religious experience[107] and may become preoccupied by thoughts of God even if they were not previously. Neuroscientist V. S. Ramachandran hypothesizes that seizures in the temporal lobe, which is closely connected to the emotional center of the brain, the limbic system, may lead to those afflicted to view even banal objects with heightened meaning.[108]

# Psychologists studying feelings of awe found that participants feeling awe after watching scenes of natural wonders become more likely to believe in a supernatural being and to see events as the result of design, even when given randomly generated numbers.[109]

# Relationship with humanity


# Praying Hands by Albrecht Dürer
# Worship
# See also: Worship, Prayer, and Supplication
# Theistic religious traditions often require worship of God and sometimes hold that the purpose of existence is to worship God.[110][111] To address the issue of an all-powerful being demanding to be worshipped, it is held that God does not need or benefit from worship but that worship is for the benefit of the worshipper.[112] Gandhi expressed the view that God does not need his supplication and that "Prayer is not an asking. It is a longing of the soul. It is a daily admission of one's weakness".[113] Invoking God in prayer plays a significant role among many believers. Depending on the tradition, God can be viewed as a personal God who is only to be invoked directly while other traditions allow praying to intermediaries, such as saints, to intercede on their behalf. Prayer often also includes supplication such as asking forgiveness. God is often believed to be forgiving. For example, a hadith states God would replace a sinless people with one who sinned but still asked repentance.[114] Sacrifice for the sake of God is another act of devotion that includes fasting and almsgiving. Remembrance of God in daily life include mentioning interjections thanking God when feeling gratitude or phrases of adoration, such as repeating chants while performing other activities.

# Salvation
# Main article: Salvation
# Transtheistic religious traditions may believe in the existence of deities but deny any spiritual significance to them. The term has been used to describe certain strands of Buddhism,[115] Jainism and Stoicism.[116]

# Among religions that do attach spirituality to the relationship with God disagree as how to best worship God and what is God's plan for mankind. There are different approaches to reconciling the contradictory claims of monotheistic religions. One view is taken by exclusivists, who believe they are the chosen people or have exclusive access to absolute truth, generally through revelation or encounter with the Divine, which adherents of other religions do not. Another view is religious pluralism. A pluralist typically believes that his religion is the right one, but does not deny the partial truth of other religions. The view that all theists actually worship the same god, whether they know it or not, is especially emphasized in the Baháʼí Faith, Hinduism[117] and Sikhism.[118] The Baháʼí Faith preaches that divine manifestations include great prophets and teachers of many of the major religious traditions such as Krishna, Buddha, Jesus, Zoroaster, Muhammad, Bahá'ú'lláh and also preaches the unity of all religions and focuses on these multiple epiphanies as necessary for meeting the needs of humanity at different points in history and for different cultures, and as part of a scheme of progressive revelation and education of humanity. An example of a pluralist view in Christianity is supersessionism, i.e., the belief that one's religion is the fulfillment of previous religions. A third approach is relativistic inclusivism, where everybody is seen as equally right; an example being universalism: the doctrine that salvation is eventually available for everyone. A fourth approach is syncretism, mixing different elements from different religions. An example of syncretism is the New Age movement.

# Epistemology
# Faith
# Main article: Faith
# Fideism is the position that in certain topics, notably theology such as in reformed epistemology, faith is superior than reason in arriving at truths. Some theists argue that there is value to the risk in having faith and that if the arguments for God's existence were as rational as the laws of physics then there would be no risk. Such theists often argue that the heart is attracted to beauty, truth and goodness and so would be best for dictating about God, as illustrated through Blaise Pascal who said, “The heart has its reasons that reason does not know.”[119] A hadith attributes a quote to God as “I am what my slave thinks of me”.[120] Inherent intuition about God is referred to in Islam as fitra, or “innate nature”.[121] In Confucian tradition, Confucius and Mencius promoted that the only justification for right conduct, called the Way, is what is dictated by Heaven, a more or less anthropomorphic higher power, and is implanted in humans and thus there is only one universal foundation for the Way.[122]

# Revelation
# Main article: Revelation
# See also: Prophet
# Revelation refers to some form of message communicated by God. This is usually proposed to occur through the use of prophets or angels. Al-Maturidi argued for the need for revelation because even though humans are intellectually capable of realizing God, human desire can divert the intellect and because certain knowledge cannot be known except when specially given to prophets, such as the specifications of acts of worship.[123] It is argued that there is also that which overlaps between what is revealed and what can be derived. According to Islam, one of the earliest revelations to ever be revealed was “If you feel no shame, then do as you wish.”[124] The term General revelation is used to refer to knowledge revealed about God outside of direct or special revelation such as scriptures. Notably, this includes studying nature, sometimes seen as the Book of Nature.[125] An idiom in Arabic states, "The Qur’an is a Universe that speaks. The Universe is a silent Qur’an".[126]

# Reason
# On matters of theology, some such as Richard Swinburne, take an evidentialist position, where a belief is only justified if it has a reason behind it, as opposed to holding it as a foundational belief.[127] Traditionalist theology holds that one should not opinionate beyond revelation to understand God's nature and frown upon rationalizations such as speculative theology.[128] Notably, for anthropomorphic descriptions such as the “Hand of God” and attributes of God, they neither nullify such texts nor accept a literal hand but leave any ambiguity to God, called tafwid, without asking how.[129][130] Physico-theology provides arguments for theological topics based on reason.[131]"""

# # Generate and print the summary
# print(generate_summary(example_text))

