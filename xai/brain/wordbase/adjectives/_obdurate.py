

#calss header
class _OBDURATE():
	def __init__(self,): 
		self.name = "OBDURATE"
		self.definitions = [u'extremely determined to act in a particular way and not to change despite what anyone else says: ', u'used to describe a person who refuses to change their mind, or someone or something that is difficult to deal with or change: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
