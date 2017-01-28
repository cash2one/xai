

#calss header
class _FURTHER():
	def __init__(self,): 
		self.name = "FURTHER"
		self.definitions = [u'more or extra: ', u'used in business letters to refer to an earlier letter, conversation, meeting, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
