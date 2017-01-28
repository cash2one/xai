

#calss header
class _FEMININE():
	def __init__(self,): 
		self.name = "FEMININE"
		self.definitions = [u'having characteristics that are traditionally thought to be typical of or suitable for a woman: ', u'belonging to the group of nouns that, in some languages, are not masculine or neuter: ', u'used to refer to a particular form of a noun in English, such as "actress", that refers only to a female person. These feminine forms are now being used less often.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
