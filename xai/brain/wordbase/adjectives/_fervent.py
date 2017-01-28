

#calss header
class _FERVENT():
	def __init__(self,): 
		self.name = "FERVENT"
		self.definitions = [u'used to describe beliefs that are strongly and sincerely felt or people who have strong and sincere beliefs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
