

#calss header
class _IMPREGNABLE():
	def __init__(self,): 
		self.name = "IMPREGNABLE"
		self.definitions = [u'A building or other place that is impregnable is so strongly built and/or defended that it cannot be entered by force: ', u'powerful and impossible to beat, especially in sport: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
