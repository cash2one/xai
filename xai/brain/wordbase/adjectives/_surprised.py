

#calss header
class _SURPRISED():
	def __init__(self,): 
		self.name = "SURPRISED"
		self.definitions = [u'feeling or showing surprise because something has happened that you did not expect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
