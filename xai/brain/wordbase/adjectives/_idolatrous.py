

#calss header
class _IDOLATROUS():
	def __init__(self,): 
		self.name = "IDOLATROUS"
		self.definitions = [u'relating to the religious practice of praying to a picture or object: ', u'showing very great admiration or respect for someone or something, often too great: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
