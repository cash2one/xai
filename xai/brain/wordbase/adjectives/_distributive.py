

#calss header
class _DISTRIBUTIVE():
	def __init__(self,): 
		self.name = "DISTRIBUTIVE"
		self.definitions = [u'(of a mathematical operation) giving the same result whether parts are acted on in combination or separately', u'(of an adjective) showing that the members of a group are to be treated separately, rather than as a group: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
