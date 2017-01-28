

#calss header
class _PERIPATETIC():
	def __init__(self,): 
		self.name = "PERIPATETIC"
		self.definitions = [u'travelling around to different places, usually because you work in more than one place: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
