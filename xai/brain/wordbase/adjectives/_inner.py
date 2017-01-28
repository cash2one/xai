

#calss header
class _INNER():
	def __init__(self,): 
		self.name = "INNER"
		self.definitions = [u'inside or contained within something else: ', u'Inner feelings or thoughts are ones that you do not show or tell other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
