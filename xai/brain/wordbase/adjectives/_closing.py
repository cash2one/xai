

#calss header
class _CLOSING():
	def __init__(self,): 
		self.name = "CLOSING"
		self.definitions = [u'coming near the end of a speech, event, activity, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
