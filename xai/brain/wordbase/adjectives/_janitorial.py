

#calss header
class _JANITORIAL():
	def __init__(self,): 
		self.name = "JANITORIAL"
		self.definitions = [u'relating to the job of being a janitor (= a person employed to look after a large building): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
