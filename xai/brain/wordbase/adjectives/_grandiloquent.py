

#calss header
class _GRANDILOQUENT():
	def __init__(self,): 
		self.name = "GRANDILOQUENT"
		self.definitions = [u'A grandiloquent style or way of using language is complicated in order to attract admiration and attention, especially in order to make someone or something seem important: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
