

#calss header
class _WORDY():
	def __init__(self,): 
		self.name = "WORDY"
		self.definitions = [u'containing too many words: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
