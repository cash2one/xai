

#calss header
class _SYMPATHETIC():
	def __init__(self,): 
		self.name = "SYMPATHETIC"
		self.definitions = [u"used to describe someone who shows, especially by what they say, that they understand and care about someone else's suffering: ", u"If a character in a book or film is sympathetic, they are described or shown in such a way that you are able to understand the character's feelings, with the result that you like them: ", u'agreeing with or supporting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
