

#calss header
class _AMATEUR():
	def __init__(self,): 
		self.name = "AMATEUR"
		self.definitions = [u'taking part in an activity for pleasure, not as a job: ', u'relating to an activity, especially a sport, where the people taking part do not receive money: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
