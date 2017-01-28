

#calss header
class _FAIR():
	def __init__(self,): 
		self.name = "FAIR"
		self.definitions = [u'treating someone in a way that is right or reasonable, or treating a group of people equally and not allowing personal opinions to influence your judgment: ', u'If something is fair, it is reasonable and is what you expect or deserve: ', u'If a game or competition is fair, it is done according to the rules: ', u'it is the right way to treat someone and what they deserve: ', u'it is true to say: ', u'considering everything that has an effect on a situation, so that a fair judgment can be made: ', u'something you say to show that you understand why someone has done or said something: ', u'something that you say when you want someone to behave reasonably or treat you the same as other people: ', u'an opportunity to explain something or give your opinions, without other people trying to influence the situation: ', u'in an honest way and without any doubt: ', u'If you hit someone fair and square on a particular part of their body, you hit that person hard, exactly on that part: ', u'(of skin) pale, or (of hair) pale yellow or gold: ', u'quite large: ', u'neither very good nor very bad: ', u'(of an idea, guess, or chance) good, but not excellent: ', u'(of weather) pleasant and dry: ', u'(of a woman) beautiful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
