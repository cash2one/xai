

#calss header
class _MEEK():
	def __init__(self,): 
		self.name = "MEEK"
		self.definitions = [u'quiet, gentle, and not willing to argue or express your opinions in a forceful way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
