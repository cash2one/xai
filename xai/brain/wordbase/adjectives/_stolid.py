

#calss header
class _STOLID():
	def __init__(self,): 
		self.name = "STOLID"
		self.definitions = [u'(of a person) calm and not showing emotion or excitement, or (of a thing) not interesting or attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
