

#calss header
class _M():
	def __init__(self,): 
		self.name = "M"
		self.definitions = [u'written abbreviation for  male adjective  (especially on forms)', u'written abbreviation for  married  (especially on family trees)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
