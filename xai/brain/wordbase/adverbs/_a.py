

#calss header
class _A():
	def __init__(self,): 
		self.name = "A"
		self.definitions = [u'used before a noun to refer to a single thing or person that has not been mentioned before, especially when you are not referring to a particular thing or person: ', u'used to say what type of thing or person something or someone is: ', u'used to mean any or every thing or person of the type you are referring to: ', u'used before some uncountable nouns when you want to limit their meaning in some way, such as when describing them more completely or referring to one example of them: ', u'used before some nouns of action when referring to one example of the action: ', u'used when referring to a unit or container of something, especially something you eat or drink: ', u'used before the first but not the second of two nouns that are referred to as one unit: ', u'used before some words that express a number or amount: ', u"used in front of a person's name when referring to someone who you do not know: ", u"used in front of someone's family name when they are a member of that family: ", u'used before the name of a day or month to refer to one example of it: ', u'one: ', u'used between a fraction and a unit of measurement: ', u'used when saying how often something happens in a certain period: ', u'used when saying how much someone earns or how much something costs in a certain period: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
