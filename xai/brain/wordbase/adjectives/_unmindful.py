

#calss header
class _UNMINDFUL():
	def __init__(self,): 
		self.name = "UNMINDFUL"
		self.definitions = [u'not remembering, noticing, or being careful about something']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
